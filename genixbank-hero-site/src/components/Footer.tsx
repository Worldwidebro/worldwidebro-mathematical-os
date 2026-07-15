export default function Footer() {
  return (
    <footer className="bg-[#F5F5F5] px-6 py-10 border-t border-black/10">
      <div className="max-w-[88rem] mx-auto flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-black/50">
        <span>© {new Date().getFullYear()} GenixBank. Part of Worldwidebro Holdings — Financial OpCo.</span>
        <span>FIN-001 · GenixBank Lite</span>
      </div>
    </footer>
  );
}
