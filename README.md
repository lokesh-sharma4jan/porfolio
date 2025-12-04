# Portfolio Website - Setup Instructions

## 🎉 Your Interactive Portfolio Website is Ready!

I've created a modern, interactive portfolio website with the following features:

### ✨ Features Included:

- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Smooth Animations** - Scroll animations, hover effects, and transitions
- **Interactive Elements**:
  - Typing effect for role/title
  - Animated skill bars with progress indicators
  - Counter animations for statistics
  - Timeline for work experience
  - Project cards with hover overlays
  - Contact form with validation
  - Back to top button
  - Scroll progress indicator
  - Mobile hamburger menu

### 📁 Files Created:

1. **index.html** - Main HTML structure
2. **styles.css** - All styling with animations
3. **script.js** - Interactive JavaScript features
4. **README.md** - This instruction file

### 🔧 How to Customize with Your Resume Details:

Since I cannot read .docx files directly, please open your **Ats97_Lokesh_Sharma_Latest.docx** file and update the following sections in `index.html`:

#### 1. **Hero Section** (Lines 25-50)

- Update your name in `<h1 class="glitch">`
- Modify roles in `script.js` (line 30) to match your job titles
- Add your profile image: Replace `profile.jpg` with your photo
- Update social media links (LinkedIn, GitHub, Twitter, Email)

#### 2. **About Section** (Lines 65-90)

- Replace the about text with your professional summary
- Update the statistics (years of experience, projects, clients)
- Ensure the resume download link points to your .docx file

#### 3. **Skills Section** (Lines 95-180)

- Add/remove programming languages based on your expertise
- Update skill percentages (data-progress values)
- Add any additional technologies you work with
- Update skill tags at the bottom

#### 4. **Experience Section** (Lines 185-235)

- Replace with your actual work experience
- Update job titles, company names, dates
- Add your real responsibilities and achievements
- Add/remove timeline items as needed

#### 5. **Projects Section** (Lines 240-320)

- Replace with your actual projects
- Add project descriptions, technologies used
- Update project links (live demo and GitHub)
- Add project images in the project folder

#### 6. **Education Section** (Lines 325-360)

- Update with your degrees and certifications
- Add university names, graduation dates
- Include any relevant coursework or honors

#### 7. **Contact Section** (Lines 365-400)

- Update email address
- Add phone number
- Add location/city
- Update social media links

### 🎨 Customization Tips:

#### Change Color Scheme (in `styles.css`):

```css
:root {
  --primary-color: #667eea; /* Change to your preferred color */
  --secondary-color: #764ba2; /* Change to your preferred color */
  --accent-color: #f093fb; /* Change to your preferred color */
}
```

#### Add Your Images:

1. Add your profile photo as `profile.jpg` in the same folder
2. Add project images as `project1.jpg`, `project2.jpg`, etc.

#### Update Typing Roles (in `script.js` line 30):

```javascript
const roles = ["Your Role 1", "Your Role 2", "Your Role 3"];
```

### 🚀 How to Run:

1. Simply open `index.html` in any modern web browser
2. Or use VS Code Live Server extension:
   - Right-click on `index.html`
   - Select "Open with Live Server"

### 📱 Testing Responsiveness:

- Open browser DevTools (F12)
- Click the device toolbar icon
- Test on different screen sizes

### 🌐 Deployment Options:

**Free Hosting Options:**

1. **GitHub Pages**

   - Create a GitHub repository
   - Push your files
   - Enable GitHub Pages in settings

2. **Netlify**

   - Drag and drop your folder
   - Get instant deployment

3. **Vercel**
   - Import from GitHub
   - Automatic deployments

### 📝 Resume Data Extraction Guide:

Open your `Ats97_Lokesh_Sharma_Latest.docx` and extract:

- [ ] Personal Information (Name, Email, Phone, Location)
- [ ] Professional Summary/Objective
- [ ] Technical Skills (Languages, Frameworks, Tools, Databases)
- [ ] Work Experience (Company, Role, Duration, Responsibilities)
- [ ] Projects (Name, Description, Technologies, Links)
- [ ] Education (Degree, University, Year, GPA if applicable)
- [ ] Certifications (Name, Issuer, Year)
- [ ] Social Media Links (LinkedIn, GitHub, Portfolio)

### 🎯 Next Steps:

1. ✅ Extract information from your resume
2. ✅ Update all sections in `index.html`
3. ✅ Add your profile photo and project images
4. ✅ Test the website locally
5. ✅ Customize colors if desired
6. ✅ Deploy to a hosting platform

### 💡 Pro Tips:

- Use high-quality images (profile photo at least 400x400px)
- Keep descriptions concise but informative
- Update project links to working demos
- Ensure all social media links are correct
- Test contact form functionality
- Check mobile responsiveness thoroughly

### 🐛 Troubleshooting:

**If animations don't work:**

- Make sure all three files are in the same folder
- Check browser console for errors (F12)

**If images don't show:**

- Verify image file names match exactly
- Check that images are in the same folder

**If styling looks broken:**

- Ensure `styles.css` is properly linked in `index.html`
- Clear browser cache and reload

### 📧 Need Help?

Feel free to ask for:

- Help with specific customizations
- Adding new features
- Fixing any issues
- Deployment assistance

---

**Happy Portfolio Building! 🎉**

Your portfolio is now ready to impress recruiters and showcase your amazing work!
