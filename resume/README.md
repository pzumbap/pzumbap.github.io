# Resume source

`content.yaml` contains all résumé text, dates, bullets, skills, and section labels. `build.py` contains the PDF layout only.

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

The command writes `Resume_PZ.pdf`, which is the same file linked from the portfolio site. The layout flows to additional pages automatically when future content no longer fits on one page.

For a draft PDF without replacing the portfolio file:

```sh
.venv/bin/python resume/build.py --output /private/tmp/Pablo_Zumba_resume_draft.pdf
```
