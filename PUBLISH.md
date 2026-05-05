# Publish

## Option 1: Create a GitHub repo and push

1. Create an empty GitHub repository, for example `paper-review-codex-skills`.
2. Run:

```powershell
cd D:\AAA项目\skill
git remote add origin https://github.com/<your-username>/paper-review-codex-skills.git
git push -u origin main
git push origin v0.1.0
```

## Option 2: Upload the release zip

Use this file as a release asset or manual upload source:

`D:\AAA项目\paper-review-codex-skills-v0.1.0.zip`

## Option 3: Web upload

If you do not want to use git on the first push:

1. Create an empty repository on GitHub.
2. Upload the contents of `D:\AAA项目\paper-review-codex-skills-v0.1.0.zip`.
3. Commit the uploaded files through the GitHub web UI.

## Recommended Repo Metadata

- Repository name: `paper-review-codex-skills`
- Description: `Codex skills for paper review, data auditing, rebuttal planning, artifact checks, and camera-ready polish.`
- Topics: `codex`, `skills`, `paper-review`, `llm`, `research`, `reproducibility`, `neurips`, `icml`
