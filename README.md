# Student Services Assistant (DEV-C02) - GLA University, Mathura

A chat assistant for a university website. It answers questions from official
circulars in English or Hindi and collects certificate requests through a guided,
form-style conversation. Requests are saved to a list that office staff can view.

Built with Python, Streamlit and the Gemini API. The circulars are sample data
created by the team, not real university documents.

## Run it (same setup as before)

1. Open this folder in VS Code. The terminal prompt must end with the folder name.
2. Install the libraries once: `python -m pip install -r requirements.txt`
3. Your `.env` file stays as it is (key and model). If you need a new one, copy
   `.env.example` to `.env` and put your Gemini key in it.
4. Start the app: `python -m streamlit run app.py`

## Pages

| Page | What it shows |
|---|---|
| Student chat | Quick-question buttons, free chat in English or Hindi, certificate request flow, office contact |
| Circulars | The documents the assistant answers from, each in an expandable box |
| Office view | Totals (Total, Pending, Done, Hindi), filter, table of requests, "Mark as Done", CSV download |
| About | Problem, solution, how it works, tech stack and the team |

## Background picture of the campus

The GLA University campus photo is already in `assets/background.png` and is used as
the background. To use a different picture, save it as `assets/background.jpg` (or
replace the png), keep it under 3 MB and refresh the browser. If there is no picture,
the app uses a navy gradient. Colours and the dark theme are in `.streamlit/config.toml`.

## What is inside

| File | Purpose |
|---|---|
| `app.py` | The whole app |
| `circulars/` | 11 sample circulars: fees, fee help, scholarships, scholarship help, attendance, exams, exam help, certificates, certificate help, B.Tech subjects and codes, office contact. Edit or add `.txt` files |
| `assets/` | `background.png` (campus photo) |
| `.streamlit/config.toml` | Theme colours |
| `check_gemini.py` | Tests your key and model: `python check_gemini.py` |
| `requests.csv` | Created automatically when the first request is saved |
| `test_questions.md` | Test questions with expected answers |

## How it works

- **Answers:** all circulars are sent to Gemini with every question, with rules to
  answer only from them, reply in the student's language, and give the office
  contact when the answer is not found.
- **Certificate request:** typing "I want a bonafide certificate" (or using the
  sidebar button) starts a guided flow: name, roll number, certificate type,
  confirmation. Each request gets a unique ID and starts as Pending.
- **Office view:** staff mark a request Done. Close `requests.csv` in Excel before
  saving new requests, because an open file can block writing.
- **Gemini slow or down:** the app waits up to 45 seconds, then shows a message with
  the office contact instead of freezing.

## Customizing

- Change the university name, team and colours near the top of `app.py`.
- Change the certificate types in the `CERTS` list.
- To use another model, set `GEMINI_MODEL` in `.env` (the last line wins).

## Troubleshooting

- `streamlit is not recognized`: run `python -m pip install -r requirements.txt`, then
  `python -m streamlit run app.py`.
- Run commands inside this project folder, not in `C:\Users\hp`.
- "model not found" or a slow reply: run `python check_gemini.py` and pick a Flash model
  from the list.
- Never share `.env` or upload it to GitHub.
