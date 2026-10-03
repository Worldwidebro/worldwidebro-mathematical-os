#!/bin/bash

echo "🚀 Mounting Network Drives (T7 Shield & LaCie) from Mac Studio over Tailscale..."

# Send mount requests to Finder
open "smb://acebless@100.87.214.70/T7 Shield"
open "smb://acebless@100.87.214.70/LaCie"

echo "⏳ Waiting for volumes to mount..."
sleep 5

# 1. Verify LaCie
if [ -d "/Volumes/LaCie" ]; then
    echo "✅ LaCie successfully mounted."
else
    echo "❌ Failed to detect /Volumes/LaCie."
fi

# 2. Verify T7 Shield & Handle Unified Brain Symlink
if [ -d "/Volumes/T7 Shield/Company Brain" ]; then
    echo "✅ T7 Shield successfully mounted."
    echo "🔗 Creating unified symlink for Company Brain..."
    
    LOCAL_PATH="/Users/acebless/Documents/The Company/Company Brain"
    BACKUP_PATH="/Users/acebless/Documents/The Company/Company Brain_LOCAL_BACKUP"
    TARGET_PATH="/Volumes/T7 Shield/Company Brain"
    
    # If it's NOT a symlink, back it up and link it
    if [ ! -L "$LOCAL_PATH" ]; then
        echo "📦 Creating backup of local folder to $BACKUP_PATH..."
        mv "$LOCAL_PATH" "$BACKUP_PATH"
        ln -s "$TARGET_PATH" "$LOCAL_PATH"
        echo "✅ Symlink created! Your local folder now secretly lives on the T7 Shield."
    else
        echo "✅ Symlink already exists. You are fully connected to the T7 Shield."
    fi
else
    echo "❌ Failed to detect /Volumes/T7 Shield/Company Brain. Please check the network."
fi
