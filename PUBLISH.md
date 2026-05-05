# Publish

## Option 1: Create a GitHub repo and push

1. Create an empty GitHub repository, for example `paper-review-codex-skills`.
2. Run:

```powershell
cd <path-to-this-repo>
git remote add origin https://github.com/<your-username>/paper-review-codex-skills.git
git push -u origin main
git push origin v0.1.0
```

## Option 2: Upload the release zip

Use this file as a release asset or manual upload source:

`paper-review-codex-skills-v0.1.0.zip`

## Option 3: Web upload

If you do not want to use git on the first push:

1. Create an empty repository on GitHub.
2. Upload the contents of `paper-review-codex-skills-v0.1.0.zip`.
3. Commit the uploaded files through the GitHub web UI.

## Recommended Repo Metadata

- Repository name: `paper-review-codex-skills`
- Description: `Portable agent skills for paper review, data auditing, rebuttal planning, artifact checks, and camera-ready polish.`
- Topics: `codex`, `agents`, `skills`, `paper-review`, `llm`, `research`, `reproducibility`, `neurips`, `icml`

## Live GitHub Quality Checklist

After the first push:

1. Open the repository homepage and confirm the README renders both images from `assets/`.
2. Open the Actions tab and wait for `Validate skills` to finish.
3. Confirm the latest workflow run is green.
4. Create a release named `v0.1.0` and upload `paper-review-codex-skills-v0.1.0.zip`.
5. Add the workflow badge below to `README.md` after replacing `<your-username>`.

## Suggested GitHub README Badges

After pushing to GitHub, the validation workflow badge can be added to `README.md`:

```markdown
[![Validate skills](https://github.com/<your-username>/paper-review-codex-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/<your-username>/paper-review-codex-skills/actions/workflows/validate.yml)
```
