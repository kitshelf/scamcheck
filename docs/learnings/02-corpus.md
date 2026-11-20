# 02 — Corpus learnings

What the learn-from library taught, and what changed in the rubric, packs, and spine because of it. The upstream records: [`../../corpus/README.md`](../../corpus/README.md), [`../../corpus/TUNING.md`](../../corpus/TUNING.md) (one owner: the tuning record), [`../../packs/README.md`](../../packs/README.md). Method: count each tell on the scam-labelled side of every vendored set against its safe/ham side; "a tell that is as common in the safe side as the scam side is not a marker, and its calibration line says so."

---

## C1 · The safe side teaches more than the scam side

**Learning.** The corpus's most useful contribution was **not** the scam tells — it was the tells that turned out to be safe-dominant. `deadline` (phish 15/498), `asap` (14/122), `registration fee` (18/125), `log in` (39/159), `tax` (286/678): all ordinary language of real life. A rubric built only from scam examples would fire on every one of them. Counting the safe side is what prevents the kit from becoming an over-flagging machine (see D4).

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Calibration findings — tells that are NOT markers; the variations pass added more safe-side lines (`action required` 0/5, `right away` 37/34, `salary` 14/85, `interview` 69/325, `resume` 67/336, `job`/`hiring`/`recruit` all safe-dominant).

**Change.** The safe-dominant phrases are written into the rubric and pack calibration conditions as *does not fire alone* lines — e.g. jobs J-U1 now says: "'Asap,' 'deadline,' 'right away,' 'action required,' and 'will be closed' are safe-side phrases; they do not fire alone" ([`../../screen/rubrics/markers-jobs.md`](../../screen/rubrics/markers-jobs.md)).

---

## C2 · Dual sourcing: corpus counts confirm or correct regulator markers — and the gaps are recorded, not papered over

**Learning.** The corpus is a second witness. Sometimes it confirms a regulator-sourced marker with overwhelming counts (`social security number` multi 486/2 → J-X2; `gift card` dlg 214/0 → J-P4; `Telegram/WhatsApp` discord 17/0 → J-I1). Sometimes it adds tells the regulators hadn't phrased (`routing number` 133/1; `processing fee`/`activation fee` 133/0, 13/0; Discord as a first-choice isolation channel). And sometimes it says **nothing** — `selfie` had zero hits in any English set, `no interview` was 2/1 — and those markers keep their regulator source, stated as such.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Attested tells, §Honest gaps. The sharpest case: the `wrong` dialogue type (the wrong-number romance opener) sits on the **safe** side (200 rows) — so the corpus does *not* evidence RO-PR1, and TUNING.md records this "so no one later claims corpus support that does not exist."

**Change.** The rubric header now carries both sources in one line — regulator sources plus "Tuned against `corpus/` (2026-11-20) scam-vs-safe; counts and method in [`corpus/TUNING.md`](../../corpus/TUNING.md)" — and the honest-gaps section exists so every marker's evidentiary basis is visible.

---

## C3 · Whole new markers can come from the corpus — the strongest signals in the library came from it

**Learning.** Two markers exist *because* the corpus demanded them, not because a regulator alert mentioned them first: **B-PR4 · the advance-fee windfall** (`next of kin` clair 1314/1, `beneficiary` 1273/2, `inherit` 439/14, `deceased client` 180/0) and **B-PR5 · the remote-access "fix"** (`remote access` 91/0, "your computer is infected" 149/0 — "the strongest single signal in the library," per the tuning record).

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §New markers added; [`../../packs/banking/markers-banking.md`](../../packs/banking/markers-banking.md).

**Change.** Both entered the **banking pack** — as alpha, with "Fixture: pending" written on them. They do not ship in a rubric until the banking family's gauntlet exists (see C4).

---

## C4 · Nothing auto-enters: the entry contract is calibration line + source + fixture

**Learning.** The corpus is an idea generator, not a rulebook. A marker enters only with (1) the tell, (2) the *not-a-marker-when* calibration line tested against the safe side, (3) a source note, and (4) a fixture that exercises it. When a fixtureless marker was found in the shipped rubric (J-PR5, task-scam pay-to-unlock), that was treated as a defect and closed — fixture 17 now exercises it.

**Evidence.** [`../../CONVENTIONS.md`](../../CONVENTIONS.md) §corpus/; [`../../packs/README.md`](../../packs/README.md) §Rules; [`../../tests/MANIFEST.md`](../../tests/MANIFEST.md) §Coverage check: "J-PR5 is planted in 17 and J-I2 in 18 — every marker in the rubric is now exercised by at least one fixture"; TUNING §Candidate markers (Discord-Nitro task scam, prize SMS) recorded and **blocked** on fixtures.

**Change.** The learn-from protocol (sample → extract → draft with calibration → review → record) and the status ladder in `packs/`: alpha pack → shipped family only when the family's fixtures and verify checklist pass the gauntlet.

---

## C5 · Compiled artifacts drift — the spine-sync defect and its fix

**Learning.** The first tuning pass updated the rubric and the packs **but not `SPINE.md`** — the compiled kit that chat users paste. Quick mode silently ran pre-tuning rules while full mode ran tuned ones. A compiled artifact is a copy, and any copy that is not regenerated in the same breath as its source *will* drift.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Spine sync (the consistency fix): "the quick mode ran pre-tuning rules while the full mode ran tuned ones."

**Change.** The spine now carries every tuned tell and calibration line from the rubric, compressed; both modes are verified in sync "tell by tell" ([`../../tests/README.md`](../../tests/README.md) §Modes and models), and quick-mode runs are recorded as first-class evidence on worked-example fixtures. The stale "18-marker" count in `screen/README.md` was corrected to 20 at the same time.

---

## C6 · The pastable budget is real and must be defended with a size pass

**Learning.** Two corpus passes grew the jobs rubric to 1,889 `wc -w` (1,665 real words) — past the ~1,500-word pastable bar that the two-paste promise depends on (D7). Compression without a method would have cost substance.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md) §Size pass (2026-11-20).

**Change.** The rubric was tightened to 1,635 `wc -w` / 1,554 real words with **zero loss of markers, calibration substance, or fixture-critical phrasings** — by moving corpus counts to TUNING.md (one owner) instead of keeping them in the rubric, and consolidating two duplicated tells into banking B-U1 where their evidence sits. The tradeoff (a strict ≤1,500 reading would force splitting the file) is recorded rather than hidden.

---

## C7 · Vendoring hygiene: text-only, no gated sets, dedup, provenance

**Learning.** Pulling 21 datasets (from a 1,051-dataset index) taught its own rules: parquet and data-pickles must convert to text before entering (never blindly unpickled; model artifacts, images, audio dropped); a 401 on download means the set does not come in; mirrors of already-vendored sets are deleted by content hash, not kept twice; and an unclear license is a hard no. Also: the phishing-URL research paper's URL tables were dropped on arrival — **URLs are not message text**, and the kit reads message text (charter: not a linkscanner).

**Evidence.** [`../../corpus/README.md`](../../corpus/README.md) §Rules for this folder, §Contents (21 vendored sets); `fetch.py`/`convert.py` enforce the rules in code by default.

**Change.** The rules are written in `corpus/README.md` and enforced by `fetch.py`; the three-tier boundary (fixtures test the kit, corpora teach the kit, runtime is never either) is a table at the top of the corpus README, and "the kit does not train on this corpus" is restated there because the charter says not a trained model.

---

## C8 · Non-English corpora: vendored, counted, deliberately not shipped

**Learning.** Substantial non-English material was vendored (Korean voice-phishing 37k+ rows across five sets, Uzbek/Russian 100k, Hinglish ~14k, Spanish, LLM-generated multilingual phishing). It was **not** counted for the shipped rules: the rules are English, and tone and idiom do not transfer — a literal tell in one language is ordinary phrasing in another.

**Evidence.** [`../../corpus/TUNING.md`](../../corpus/TUNING.md): "Non-English sets… are not counted here: the shipped rules are English. The Indian call set is cited once, for its own `scam_category` labels"; [`../../ROADMAP.md`](../../ROADMAP.md) §Deferred: non-English marker libraries "waits for a real user base in a second language."

**Change.** None shipped — which is the change: the deferral is recorded in the roadmap with its reason, and the corpora wait in the library for the day a real second-language user base makes them load-bearing.
