# Data Science Portfolio Template

A ready-to-deploy static portfolio website for data science students. Write your content in simple YAML files, run one command to build, and publish to GitHub Pages — no web-development experience required.

**What you get out of the box:**
- A professional single-page site with an About section, project cards, and contact links.
- Light and dark themes you can switch with one config line.
- Two example projects that demonstrate how to write clearly for a hiring-manager audience.

---

## Quick start

```bash
uv sync
uv run python build.py
uv run python serve.py   # opens http://localhost:8000 in your browser
```

---

## How to customize this portfolio

### 1. Set up the environment

Install `uv` (if you don't have it):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Install the project dependencies:

```bash
uv sync
```

### 2. Preview the demo site

Build the example site and open it locally:

```bash
uv run python build.py
uv run python serve.py
```

`serve.py` will open `http://localhost:8000` in your browser automatically.
Press `Ctrl+C` in the terminal to stop the server.

---

### 3. Create your own content

> **Do not overwrite the example files.** Copy them and edit the copies so
> you always have a working reference to look back at.

#### Step 1 — Create your student profile

```bash
cp content/example_student.yaml content/my_profile.yaml
```

Open `content/my_profile.yaml` and fill in:

| Field | Description |
| --- | --- |
| `name` | Your full name |
| `tagline` | One-line description of your focus (e.g. "Data Scientist \| Healthcare Analytics") |
| `about` | One or more paragraphs about you — supports Markdown (see below) |
| `email` | Your email address (or remove the line to hide it) |
| `linkedin` | Your LinkedIn profile URL *(optional — remove the line to hide it)* |
| `github` | Your GitHub profile URL *(optional — remove the line to hide it)* |

**Writing multi-paragraph `about` text**

The `about` field supports Markdown. Use `|` (literal block) in your YAML so blank lines and formatting are preserved:

```yaml
# Use | to write multiple paragraphs and Markdown formatting
about: |
  First paragraph here. *This text will be italic.*

  Second paragraph here. **This text will be bold.**

# Don't use > — it collapses everything into a single line,
# so blank lines between paragraphs are lost.
```

Then open `portfolio_config.yaml` and change:

```yaml
student_file: content/my_profile.yaml
```

#### Step 2 — Create your project files

```bash
cp content/projects/example_project_1.yaml content/projects/my_project_1.yaml
```

Fill in each field:

| Field | Description |
| --- | --- |
| `title` | Project name |
| `short_summary` | 2–3 sentences for a non-expert (this is the most important field!) |
| `tech_stack` | List of tools / languages used |
| `problem_statement` | The business or research problem you solved |
| `approach` | How you approached the problem |
| `results_impact` | Concrete outcomes — numbers, decisions made, lessons learned |
| `repo_url` | Link to your GitHub repository *(optional — remove the line to hide the button)* |
| `notebook_url` | Link to a specific Jupyter notebook in the repo *(optional — remove the line to hide the button)* |
| `image_path` | Place your image in `static/img/` and write `img/my_image.png` here |

Add each project to `portfolio_config.yaml`:

```yaml
projects:
  - content/projects/my_project_1.yaml
  - content/projects/my_project_2.yaml
```

Once you have your own projects listed, remove the `example_project_*.yaml` lines.

#### Step 3 — Add your own images

Replace the placeholder images by saving your own image files to `static/img/` and updating `image_path` in the corresponding project YAML. Any common image format (`.png`, `.jpg`, `.svg`) will work.

---

### 4. Customize the look and feel

#### Switch theme

In `portfolio_config.yaml`:

```yaml
theme: light    # or: dark, msu-light, msu-dark
```

The following themes are included out of the box:

| Theme name | Description |
| --- | --- |
| `light` | Clean light theme (default) |
| `dark` | Dark gray theme |
| `msu-light` | Michigan State University — Spartan Green on white |
| `msu-dark` | Michigan State University — white and Lime Green on deep green |

MSU colors follow the official brand guidelines at [brand.msu.edu/visual/color-palette](https://brand.msu.edu/visual/color-palette).

#### Modify global styles

Edit `static/css/base.css` to change layout, spacing, typography, or any style that should apply to both themes.

#### Create a custom theme

1. Copy an existing theme file:

   ```bash
   cp static/css/themes/light.css static/css/themes/ocean.css
   ```

2. Edit the colors in `ocean.css`.

3. Select it in `portfolio_config.yaml`:

   ```yaml
   theme: ocean
   ```

4. Rebuild:

   ```bash
   uv run python build.py
   ```

---

### 5. Publish with GitHub Pages

> **Before you push:** The `docs/` folder is not included in this template repo — you need to generate it first. Run `uv run python build.py` locally and commit the resulting `docs/` folder before enabling GitHub Pages, otherwise GitHub will have nothing to serve.

1. **Remove `docs/` from `.gitignore`.**

   The template's `.gitignore` excludes `docs/` so the example site isn't committed to the template repo itself. In your own fork, you need to track `docs/` so GitHub Pages can serve it. Open `.gitignore` and delete (or comment out) this line:

   ```gitignore
   docs/
   ```

2. **Build the site and commit `docs/`.**

   ```bash
   uv run python build.py
   git add docs/
   git commit -m "build site"
   ```

3. **Push your repo to GitHub.**

4. In your repository on GitHub, go to **Settings → Pages**.

5. Under **Build and deployment → Source**, select **Deploy from a branch**.

6. Set the branch to `main` (or your default branch) and the folder to `/docs`.

7. Click **Save**. GitHub will build and publish your site within a minute or two.

Your site will be available at:

```
https://<your-github-username>.github.io/<your-repo-name>/
```

> **Note:** If you name the repository `<your-github-username>.github.io`, GitHub will publish it at `https://<your-github-username>.github.io/` (no repo name suffix).

**Already have a personal site at `https://<username>.github.io/`?**

That site lives in a special repo named exactly `<username>.github.io`. As long as you put this portfolio in *any other repo* (e.g. `data-science-portfolio`), GitHub Pages will publish it alongside your existing site at a separate URL — the two sites will not interfere with each other:

| Repo name | Published URL |
| --- | --- |
| `username.github.io` | `https://username.github.io/` ← your existing site, untouched |
| `data-science-portfolio` | `https://username.github.io/data-science-portfolio/` ← this portfolio |

Because this template uses only relative paths for CSS and images, **no code changes are needed** — the site will work correctly whether it is served from the root or from a subdirectory.

---

## Typical iteration workflow

When you're making updates, the typical workflow will be:

1. Edit YAML content files and/or CSS.
2. `uv run python build.py` ← regenerate the site with your changes
3. `uv run python serve.py` ← preview in browser
4. `git add . && git commit -m "update portfolio"` ← commit your changes
5. `git push origin main` ← GitHub Pages auto-deploys

---

## Files you will edit most

| File | What it controls |
| --- | --- |
| `portfolio_config.yaml` | Theme (`light`/`dark`/`msu-light`/`msu-dark`), student file, project list, `site_title` (browser tab text) |
| `content/my_profile.yaml` | Your name, tagline, about blurb, contact info |
| `content/projects/my_project_*.yaml` | Individual project descriptions |
| `static/img/` | Your project thumbnail images |
| `static/css/base.css` | Global layout and typography |
| `static/css/themes/light.css` | Light theme colors |
| `static/css/themes/dark.css` | Dark theme colors |

Files you should **not** need to edit unless you want to change the page structure:
- `templates/base.html` — HTML shell (header, nav, footer)
- `templates/index.html` — Page layout and section order
- `build.py` — Site generator
- `serve.py` — Local preview server

---

## Project structure

```
├── pyproject.toml              # Python dependencies (managed by uv)
├── portfolio_config.yaml       # Main site config — start here
├── build.py                    # Site generator script
├── serve.py                    # Local preview server
├── content/
│   ├── example_student.yaml    # Example student profile
│   └── projects/
│       ├── example_project_1.yaml
│       └── example_project_2.yaml
├── templates/
│   ├── base.html               # HTML shell (header, nav, footer)
│   └── index.html              # Page content template
├── static/
│   ├── css/
│   │   ├── base.css            # Layout styles (all themes)
│   │   └── themes/
│   │       ├── light.css
│   │       ├── dark.css
│   │       ├── msu-light.css
│   │       └── msu-dark.css
│   └── img/
│       ├── placeholder_project_1.png
│       └── placeholder_project_2.png
└── docs/                       # Generated output — served by GitHub Pages
```

## License

This project is released under the [MIT License](LICENSE). You are free to use, modify, and distribute it — including for your own portfolio. See the `LICENSE` file for full terms.

---

## Note about AI assistance

This project was drafted and built with the help of AI ([Claude](https://claude.ai)). The initial code and structure were generated by the model based on the provided instructions that aligned with the goals for this repository. The generated content and code has been reviewed and edited to ensure quality and correctness.
