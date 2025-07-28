# 📝 Django Blogger Project

A modern, full-featured blog application built with Django. This project includes blog creation, editing, deletion (soft delete), image uploads, tag/category filtering, and user authentication.

---

## 🚀 Features Implemented

### ✅ Core Blog Functionality

- Create blog posts with:
  - Title
  - Content
  - Slug
  - Cover image (with preview before submission)
  - Categories and Tags (many-to-many)
- Read/view blog detail pages
- Update/edit blogs (only by the author)
- Soft delete blog posts (deletes are reversible)
- Slug-based blog URLs

---

### 👤 Authentication & Authorization

- Django built-in user system
- User login/logout
- Superuser creation/reset
- Author-only access for editing/deleting their own blogs

---

### 📁 Pages & Views

- `All Blogs` page with:
  - List of published blogs
  - View / Edit / Delete buttons (based on author ownership)
- `My Blogs` page:
  - Lists only blogs created by the currently logged-in user
  - “Create New Blog” button
- Blog detail view (slug-based route)
- Blog creation and blog edit forms with modern UI (CSS styled)

---

### 🖼️ Media Features

- Cover image upload for each blog post
- Real-time image preview before blog submission

---

### 🏷️ Tag & Category Support

- Blogs can have multiple tags and one category
- Filtering blogs by category or tag in the list view

---

