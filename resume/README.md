# Resume and career materials

Target: **Data Engineer**, using the employment history in this repository and the platform figures Pablo supplied: 50+ clients, 15 POS systems and variants, and tens of gigabytes per day.

[`content.yaml`](content.yaml) is the editable resume source. [`build.py`](build.py) renders a single-column PDF and a matching plain-text version. The current content fits on one US Letter page with 10-point body text, selectable text, standard headings, and contact information in the document body.

## Outputs

- [Resume PDF](../Resume_PZ.pdf): the file already linked from the portfolio site.
- [Plain-text resume](../Resume_PZ.txt): for copying into application forms.
- [ATS strategy and top five job titles](career-materials/01-ats-and-job-fit.md).
- [Cover letter](career-materials/02-cover-letter.md): an explicitly labeled AHEAD example because no employer was specified.
- [Interview follow-up emails](career-materials/03-interview-follow-up.md): replace interview-specific fields before sending.
- [LinkedIn headline, About, and experience](career-materials/04-linkedin.md).
- [Ten interview questions and STAR answers](career-materials/05-interview-prep.md): documented experience and hypothetical technical scenarios are labeled separately.
- [Evidence notes and retained background](career-materials/06-evidence-notes.md).

## Build

To update the résumé:

1. Edit `content.yaml`.
2. Install the generator dependencies once:

   ```sh
   python3 -m venv .venv
   .venv/bin/pip install -r resume/requirements.txt
   ```

3. Export the portfolio PDF:

   ```sh
   .venv/bin/python resume/build.py
   ```

The command writes `Resume_PZ.pdf` and `Resume_PZ.txt` at the repository root. Rebuild both after changing the source. The layout flows to additional pages automatically when future content no longer fits; inspect the new page count and layout after edits.

For a draft PDF without replacing the portfolio file:

```sh
.venv/bin/python resume/build.py --output /private/tmp/Pablo_Zumba_resume_draft.pdf
```

This also writes `/private/tmp/Pablo_Zumba_resume_draft.txt`. Use `--text-output PATH` to choose a different text destination, or `--content PATH` to render an alternate YAML source with the same structure.

## Review

Confirm that copied or extracted PDF text contains the name, contact details, job titles, employers, dates, degrees, and metrics in reading order. Check the page visually for clipping and crowding. Inspect the fields populated after an application upload; local text extraction cannot certify behavior in a specific employer's ATS.

The source intentionally distinguishes professional experience from academic tools and does not invent missing metrics, tools, or seniority. The supporting documents explain the evidence and keyword choices. No applications, messages, or LinkedIn changes are performed by the build.
