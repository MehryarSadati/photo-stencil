# Photo Stencil Generator  

## 📝 Overview  
This repository contains a **simple** Python script that converts images into stencil-like artwork, suitable for DIY projects, quick mockups, or fine-line tattoo designs. The code processes an input image and applies filters to create a stylized, simplified version that resembles a stencil or posterized effect.  

## 🛠 How It Works  
1. **Input Image**: Provide any image (JPG, PNG, etc.).  
2. **Processing**: The script applies edge detection, thresholding, and posterization to simplify the image into a black-and-white or limited-color stencil.  
3. **Output**: The result is a simplified, high-contrast image that can be used for basic stencil cutting, painting, or design mockups.  

### ⚠️ Important Notes  
- **This is a very simple project**—results may not be perfect and might require manual touch-ups in an image editor (e.g., cleaning up edges, adjusting contrast).  
- **I strongly believe in supporting real artists.** This tool is intended for minor, non-commercial use only—such as personal crafts, quick prototypes, or educational purposes. If you need professional-quality artwork, **please commission an actual artist** instead of relying on automated tools.  
- **Fine-line tattoos?** While this could work as a base for simple tattoo designs, always consult a professional tattoo artist for refinements and proper adaptation to skin.  

### ❓ When to Use This  
- You need a quick placeholder for a project.  
- You're experimenting with DIY crafts and have no other options.  
- It's for personal, non-commercial use (e.g., homemade stickers, simple tattoo drafts).  

### 🚫 When NOT to Use This  
- For professional or commercial work (pay an artist instead!).  
- To replicate or replace original artwork.  
- If you have the means to support real creators.  

## 🔜 Coming Soon  
- **GUI Version**: A more user-friendly interface is in the works for those who prefer not to use the command line.  

## 🛠 Installation & Usage  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/MehryarSadati/photo-stencil.git  
   cd photo-stencil  
   ```  
2. Install dependencies (OpenCV, NumPy, Pillow):  
   ```bash  
   pip install opencv-python numpy pillow 
   ```  
3. Run the script:  
   ```bash  
   python stencil_generator.py --input your_image.jpg --output stencil_result.png  
   ```  

**Remember: Automation is no substitute for human creativity. Support artists whenever possible!** 