#!/usr/bin/env python3
"""
Fashion Design OS — Product Extraction Pipeline
Isolate every garment/SKU from a fashion collage into individual product shots.

Proven on the Angels in Daylight (EC-001) reference boards: rembg removes the
background (works on white AND dark boards with enough contrast), then a
distance-transform watershed splits touching garments that connected-components
would otherwise merge.

SHARED CAPABILITY — reused by:
  ec-030-ai-product-photographer   (extraction + clean packshots)
  ec-072-ai-product-cataloger      (extraction feeds the catalog)
  ec-053-ai-visual-merchandiser    (gallery / merchandising)
  ec-012-fashion-designer-ai       (design asset library)

Usage:
  python3 extract_products.py <input_image.png> [--out DIR] [--min-distance 55]

Requires: rembg, onnxruntime, opencv-python, scikit-image, scipy, numpy
  pip install rembg onnxruntime opencv-python scikit-image scipy numpy
"""
import os, sys, argparse, glob
import cv2, numpy as np
from rembg import remove, new_session
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import watershed

_SESS = None
def session():
    global _SESS
    if _SESS is None:
        # isnet-general-use keeps ALL foreground objects (u2net keeps only the salient one)
        _SESS = new_session("isnet-general-use")
    return _SESS

def alpha_for(img_bgr, cache_path=None):
    """Return the rembg alpha (foreground) mask for an image."""
    if cache_path and os.path.exists(cache_path):
        return cv2.imread(cache_path, cv2.IMREAD_GRAYSCALE)
    rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    a = remove(rgb, session=session())[:, :, 3]
    if cache_path:
        cv2.imwrite(cache_path, a)
    return a

def extract(input_path, out_dir, min_distance=55, min_frac=0.0014, pad=8, prefix=None):
    img = cv2.imread(input_path)
    if img is None:
        raise SystemExit(f"Cannot read {input_path}")
    H, W = img.shape[:2]; area = H * W
    stem = prefix or os.path.splitext(os.path.basename(input_path))[0]

    alpha = alpha_for(img, cache_path=os.path.join(out_dir, f"_{stem}_alpha.png"))
    cov = (alpha > 60).mean()
    if cov < 0.15:
        print(f"[WARN] {stem}: low foreground coverage ({cov*100:.1f}%) — "
              f"likely a dark-on-dark board. Extraction may be poor.")

    m = (alpha > 60).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN,
                         cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    dist = ndi.distance_transform_edt(m)
    coords = peak_local_max(dist, min_distance=min_distance, labels=m, exclude_border=False)
    seeds = np.zeros(dist.shape, bool); seeds[tuple(coords.T)] = True
    markers, _ = ndi.label(seeds)
    labels = watershed(-dist, markers, mask=m)

    boxes = []
    for lbl in range(1, labels.max() + 1):
        ys, xs = np.where(labels == lbl)
        if len(xs) == 0:
            continue
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        if (x1 - x0) * (y1 - y0) < min_frac * area or (x1 - x0) < 40 or (y1 - y0) < 40:
            continue
        boxes.append((x0, y0, x1, y1))
    boxes.sort(key=lambda b: (round(b[1] / (H * 0.07)), b[0]))

    os.makedirs(out_dir, exist_ok=True)
    for n, (x0, y0, x1, y1) in enumerate(boxes, 1):
        X0, Y0 = max(0, x0 - pad), max(0, y0 - pad)
        X1, Y1 = min(W, x1 + pad), min(H, y1 + pad)
        cv2.imwrite(os.path.join(out_dir, f"{stem}-{n:02d}.png"), img[Y0:Y1, X0:X1])
    print(f"{stem}: {len(boxes)} products  (coverage {cov*100:.0f}%)")
    return len(boxes)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", help="image file(s) or glob")
    ap.add_argument("--out", default="separated")
    ap.add_argument("--min-distance", type=int, default=55,
                    help="min pixels between product centers; lower = more splits")
    args = ap.parse_args()
    files = []
    for p in args.inputs:
        files.extend(glob.glob(p))
    total = 0
    for f in files:
        total += extract(f, args.out, min_distance=args.min_distance)
    print(f"TOTAL: {total} products from {len(files)} image(s)")
