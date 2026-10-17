# ledger_GM_PLAN: c1_1 / c2_1 rewrite (design.md section 5.1)

## Files and method
- Originals (read-only, unchanged; A1 sha256 verified): /home/user/megato/prompt_originals_f6b87082/c1_1_GM_PLAN__Antigravity_gemini-4-argon-high.txt and /home/user/megato/prompt_originals_f6b87082/c2_1_GM_PLAN__Antigravity_gemini-4-argon-high.txt.
- Enhanced (same names): /home/user/megato/prompt_enhanced_f6b87082/c1_1_GM_PLAN__Antigravity_gemini-4-argon-high.txt (246 lines) and /home/user/megato/prompt_enhanced_f6b87082/c2_1_GM_PLAN__Antigravity_gemini-4-argon-high.txt (262 lines).
- Built by /tmp/claude-0/-home-user-megato/00d38b86-a9d4-564d-acaf-a8727e1b998d/scratchpad/enhance/build_GM_PLAN/build.py. Each new block is the design.md text fence, copied byte-for-byte (the script selects it by label and asserts the match is unique). Each verbatim or slot line is copied by line range from the matching original. The only text the script composes is the single space that appends the SELF-CHECK fence to PL:24 (5.1 step 7).
- Checked by /tmp/claude-0/-home-user-megato/00d38b86-a9d4-564d-acaf-a8727e1b998d/scratchpad/enhance/build_GM_PLAN/verify.py (section 8 checks A1, A3-A9, A11, A14, A15).

## Enhanced layout (section 5.1 order; enhanced line numbers c1 / c2)
| Step | Block | Source | c1 | c2 |
|---|---|---|---|---|
| 1-2 | TRIOPLUS_ROLE_CONTRACT_V2 header + GM identity line | PL:1-7 verbatim (line 3 = slot) + 3.16 | 1-8 | 1-8 |
| 3 | FLOW_POSITION_V1 + GM_PLAN role line | 3.1 | 10-13 | 10-13 |
| 4 | PRECEDENCE_V1 | 3.2 | 15-22 | 15-22 |
| 5 | TRIOPLUS_RESEARCH_QUALITY_V1 | PL:9 + 3.3 ASSIGNMENT FIRST + PL:11-13 | 24-28 | 24-28 |
| 6 | ROLE_WORKFLOW=GM_PLAN | PL:14-15 verbatim | 30-31 | 30-31 |
| 7 | GM_RESEARCH_DESIGN_V1 | PL:17-24 verbatim, SELF-CHECK sentence appended to PL:24 | 33-40 | 33-40 |
| 8 | GM_PLAN_SPEC_RULES_V1 | 5.1 fence | 42-52 | 42-52 |
| 9 | GM_PLAN_SEALED_TEXT_RULES_V1 | 5.1 fence | 54-60 | 54-60 |
| 10 | GM_PLAN_SELECTION_V1 | 5.1 fence | 62-69 | 62-69 |
| 11 | GEMINI_4_ARGON_RESEARCH_ROLE_CONTRACT_V1 role=GM + PLAN phase line | 3.17 | 71-73 | 71-73 |
| 12 | GEMINI_4_ARGON_GM_PLAN_LEAN | PL:29-33 verbatim | 75-79 | 75-79 |
| 13 | GM_EXECUTION_RULES_V1; TRANSPORT_NON_INTERACTIVE | 3.18; PL1:164-166 / PL2:179-181 verbatim | 81-84; 86-88 | 81-84; 86-88 |
| 14 | GM_READONLY_FINAL_OVERLAY (GM_PLAN variant) | 3.10 | 90-113 | 90-113 |
| 15 | HOST_CONTROL_PLANE_OWNERSHIP (GM_PLAN variant) | 3.9 | 115-119 | 115-119 |
| 16 | RESOURCE_BUDGET_GM_V1 (GM_PLAN variant) | 3.8 | 121-122 | 121-122 |
| 17 | CAMPAIGN_GOAL_DIRECTIVE (GM_PLAN variant) | 3.11 | 124-129 | 124-129 |
| 18 | HTS_BACKTEST_PROGRESS (GM variant); CONVERGENCE_V1 | 3.12; PL1:51-59 / PL2:64-72 verbatim | 131-135; 137-145 | 131-135; 137-145 |
| 19 | HOST_OOS_MEMBERSHIP_PACKET (GM variant) | 3.14 | 147-148 | 147-148 |
| 20 | LANE_PERSONA (GM_PLAN variant) | 3.15 | 150-151 | 150-151 |
| 21 | [GM_INPUT_READ_GUIDE] slot; INDEX_USE_RULE_V1 | PL1:168-172 / PL2:183-188; 3.19 | 153-157; 159-164 | 153-158; 160-165 |
| 22 | MULTIPLE_TESTING_CONSTANTS_V1 slot; MULTIPLE_TESTING_GUARD_V1 | PL1:174-177 / PL2:190-193; 3.20 | 166-169; 171-175 | 167-170; 172-176 |
| 23 | ASSIGNED_TASK slot | PL1:34-43 + PL1:63-108 / PL2:34-56 + PL2:76-123 | 177-232 | 178-248 |
| 24 | GM_PLAN_OUTPUT_SCHEMA_V1 | 5.1 fence | 234-246 | 250-262 |

## (a) ISSUE ids applied and where
Lines are enhanced line numbers. Static blocks have the same numbers in c1 and c2 up to line 151. Where they differ, both are given as c1/c2.

| ISSUE | Status (design) | Where it is applied (block, enhanced line) |
|---|---|---|
| ISSUE-01 | FIX | PRECEDENCE_V1 15-22 is the only conflict rule, with the V2 reading at 22 (SCORECARD_V1 bad/good fields are telemetry; economics_verdict follows decision_policy). Legacy text is ranked 5 in the HTS GM variant Label line 134 "(legacy default, PRECEDENCE_V1 rank 5)", the PLAN phase line 73 and GM_PLAN_SELECTION_V1 line 63. |
| ISSUE-02 | FIX + OD-01, OD-02 | GM_PLAN_SEALED_TEXT_RULES_V1 RESOLUTION CONDITION line 56 (forward rule: one Beta-settleable boolean; for a sealed condition with alpha_beta_* clauses, copy it verbatim, Beta reports those NOT_EVALUABLE_IN_CLEAN_ROOM, Gamma measures them). The sealed c2 string stays verbatim (c2 line 187). |
| ISSUE-03 | FIX + OD-03 | GM_PLAN_SPEC_RULES_V1 CROSS-LANE PARITY line 46 (bad_rate = bad_count / n_resolved unless the goal defines it otherwise; never redefine a key). PRECEDENCE_V1 rank-2 definition tie rule, line 18. |
| ISSUE-06 | FIX + OD-17 | HTS_BACKTEST_ANALYZE removed from PLAN (ANALYZE-only, PL1:127-131 / PL2:142-146). PRECEDENCE_V1 V2 reading, line 22. |
| ISSUE-07 | FIX | GM_PLAN_SEALED_TEXT_RULES_V1 BETA FILE line 57: lane instructions name lane_result.json; *_LANE_RESULT.json names belong to the Host and ANALYZE. Sealed c2 line 196 stays verbatim (ISSUE-69). |
| ISSUE-08 | FIX | GM_PLAN_SPEC_RULES_V1 SELF-CONTAINED line 43. |
| ISSUE-09 | FIX | GM_PLAN_SPEC_RULES_V1 ONE CONDITION line 44, plus the SELF-CHECK sentence appended to line 40 ("each challenger differs from its baseline only in the clause method_delta names"). |
| ISSUE-10 | FIX | GM_PLAN_SPEC_RULES_V1 CROSS-LANE PARITY line 46. SELF-CHECK sentence, line 40 (same row counts, canonical row base and estimator definitions in all three lane instructions). |
| ISSUE-11 | FIX (PL part) | GM_PLAN_SPEC_RULES_V1 SELF-CONTAINED line 43 ("whether each threshold is pinned or TRAIN-fitted (with procedure and granularity)"). |
| ISSUE-12 | FIX + OD-04 | MULTIPLE_TESTING_GUARD_V1 at 171-175 / 172-176, directly after the verbatim MULTIPLE_TESTING_CONSTANTS_V1 slot. |
| ISSUE-13 | FIX (GM part) | INDEX_USE_RULE_V1 at 159-164 / 160-165: non-candidate rows are a lane scorecard-layout gap. |
| ISSUE-16 | FIX + OD-13 | GM_PLAN_SPEC_RULES_V1 GAMMA RECIPES line 49. GM_PLAN_OUTPUT_SCHEMA_V1 lane bullet 241 / 257 (Gamma's dependency is stated inside gamma.instruction). |
| ISSUE-21 | FIX + OD-14 | RESOURCE_BUDGET_GM_V1 PL variant 121-122; FLOW_POSITION_V1 line 11 ("50% of the PC each"); GM_PLAN_SPEC_RULES_V1 RESOURCES line 51; GM_PLAN_OUTPUT_SCHEMA_V1 evaluation_contract bullet 240 / 256 (BACKTEST_MAX_HARDWARE only as RESOURCE_BUDGET_GM_V1 allows). |
| ISSUE-22 | FIX + OD-32 | GM_PLAN_SPEC_RULES_V1 CLEAN ROOM line 48. beta.inputs_forbidden in GM_PLAN_OUTPUT_SCHEMA_V1, 241 / 257. |
| ISSUE-23 | FIX + OD-11 | HTS GM variant CYCLE_IMPROVE line 135 (datum read/add is a lane permission scoped by DATUM; GM reads datum metadata only and plans no add/edit/replace/delete). LANE_PERSONA line 151. GM_EXECUTION_RULES_V1 TOOLS line 82 (datum read as Host-listed metadata only). GM_READONLY_FINAL_OVERLAY override sentence, line 113. GM_PLAN_SPEC_RULES_V1 lane-requirements bullet, line 52. |
| ISSUE-25 | FIX | Role variants: GM_READONLY_FINAL_OVERLAY 90-113, HOST_CONTROL_PLANE_OWNERSHIP 115-119, CAMPAIGN_GOAL_DIRECTIVE 124-129, HTS GM variant 131-135, HOST_OOS GM variant 147-148, LANE_PERSONA 150-151, GEMINI GM contract 71-73. Removed as role-irrelevant: the TP branches and the ANALYZE sentence of PL:27-28, the TP sentence of PL:10, and the HTS_BACKTEST_ANALYZE block. |
| ISSUE-26 | FIX + OD-26, OD-29 | GM_PLAN_OUTPUT_SCHEMA_V1 234-246 / 250-262 is the single consolidated skeleton; "schema" key included (OD-29). The GM identity line (line 8) points to this schema. RESOURCE_BUDGET_GM_V1 121-122 settles "measured allocation" vs "do not restate BACKTEST_MAX_HARDWARE". |
| ISSUE-30 | FIX (PL part) | Shared GEMINI GM contract line 72: "Gamma runs the same model as GM, so GM-Gamma agreement is not independent model evidence." The main fix is in AN. |
| ISSUE-31 | FIX | GM_PLAN_SEALED_TEXT_RULES_V1 CYCLE 1 BOOTSTRAP, line 59. |
| ISSUE-32 | FIX | GM_PLAN_SEALED_TEXT_RULES_V1 SEALED COPY, line 55. The template slot stays verbatim (auditor proposal rejected, design 1.1). |
| ISSUE-33 | FIX + OD-06, OD-07 (PL: no text change) | Per 5.1 step 18, PL keeps CONVERGENCE_V1 verbatim at 137-145. The GAP_VECTOR sign, row shape and binding_gate ranking are defined in the lane and ANALYZE blocks (parity table row "GAP_VECTOR, binding_gate": GM_PLAN = CONVERGENCE_V1). |
| ISSUE-34 | FIX + OD-08 (PL part) | GM_PLAN_SPEC_RULES_V1 NOT MEASURABLE, line 47. |
| ISSUE-35 | FIX + OD-08 (PL part) | GM_PLAN_SPEC_RULES_V1 SELF-CONTAINED line 43 ("Give a formula for every metric used in a gate, a resolution_condition or an attack"). |
| ISSUE-36 | FIX | HTS GM variant Label line 134 (legacy default, rank 5). GM_PLAN_SELECTION_V1 line 63 ("State step 1's Bad label as the goal snapshot defines it (the +0.15% text is the legacy default)"). PLAN phase line 73. Labels in the CROSS-LANE PARITY list, line 46. |
| ISSUE-37 | FIX + OD-23 | GM_EXECUTION_RULES_V1 GROUNDING, line 84. |
| ISSUE-40 | FIX | GM_EXECUTION_RULES_V1 TOOLS line 82. GEMINI contract pointer "(GM_EXECUTION_RULES_V1 TOOLS says what remains allowed)", line 72. |
| ISSUE-41 | FIX + OD-30 | GM_EXECUTION_RULES_V1 OUTPUT, line 83. The per-call limit sentence stays only in LEAN, line 76 (ISSUE-70). |
| ISSUE-42 | FIX | INDEX_USE_RULE_V1 at 159-164 / 160-165. The truncated c2 ids stay verbatim (ISSUE-69). |
| ISSUE-43 | FIX + OD-24, OD-25 | GM_PLAN_SELECTION_V1 62-69 (cycle 1 / cycle 2 reading, stall vs REQUIRED_RESEARCH_ANGLE, research_angle order, exactly one target_criteria ID, Host dependency order). CAMPAIGN_GOAL_DIRECTIVE line 128 ("choose research_angle by GM_PLAN_SELECTION_V1"). |
| ISSUE-46 | FIX + OD-27 | GM_PLAN_OUTPUT_SCHEMA_V1 FAILURE bullet, 246 / 262. |
| ISSUE-47 | FIX (main fix in AN, GM_ANALYZE_NOMINATION_V1) | PL side: the GM_PLAN_OUTPUT_SCHEMA_V1 SECTION REUSE bullet (245 / 261) gives ANALYZE explicit $inherit markers and never relies on omission. |
| ISSUE-48 | FIX | GM_PLAN_OUTPUT_SCHEMA_V1 SECTION REUSE, 245 / 261. |
| ISSUE-49 | FIX | GM_PLAN_SEALED_TEXT_RULES_V1 BRANCHES, line 58. |
| ISSUE-50 | FIX + OD-23 | GM_EXECUTION_RULES_V1 GROUNDING, line 84. |
| ISSUE-51 | FIX + OD-31 | FLOW_POSITION_V1 10-13 with the GM_PLAN role line 13. BOT_LANE_MODE is clarified on line 12. |
| ISSUE-60 | FIX | GM_PLAN_SPEC_RULES_V1 EXPLORATION, line 45. |
| ISSUE-61 | FIX | GM_PLAN_SELECTION_V1 target_criteria bullet, line 67 (exactly one ID satisfies both "1-3, prefer 1" and "exactly one"). |
| ISSUE-62 | FIX + OD-28 | GM_PLAN_SEALED_TEXT_RULES_V1 HOST/LANE ACTION, line 60. |
| ISSUE-67 | FIX | The consolidations are listed in (d). The main ones: HOST_CONTROL worker lines removed; the ICV rule stated once (HOST_CONTROL line 117; PL1:149 / PL2:164 removed); TARGET_FORMULA_REGISTRY absence stated once (line 118; PL1:151 / PL2:166 removed); the "Do not edit next_goal.txt" duplicates (PL:26, PL1:122 / PL2:137, PL1:125 / PL2:140) folded into CAMPAIGN line 125; the GM compute rule kept once in the read-guide slot (PL1:172 / PL2:188; PL1:61 / PL2:74 removed); the Flow line moved once into FLOW_POSITION_V1. |
| ISSUE-68 | FIX | Static lines PL1:44-62 / PL2:57-75 moved out of the slot region (5.1 step 23). A4: all 60 lines that differ between enhanced c1 and c2 are listed slot lines. |
| ISSUE-69 | KEEP_AS_IS_WITH_REASON | All sealed values stay verbatim; README items are listed in (f). |
| ISSUE-70 | KEEP_AS_IS_WITH_REASON | "Gemini 4 Argon High has a 65,536 per-call output token limit." stays verbatim, only in LEAN (line 76). New text names no limit numbers. |

OD-38 (progress_review arrays) is applied in the GM_PLAN_OUTPUT_SCHEMA_V1 progress_review bullet (243 / 259). The ALPHA DISCOVERY bullet (line 50) routes discovery to NEW_CANDIDATES only, which matches the ISSUE-38 fix in AL and AN. ISSUEs whose files do not include PL and whose decisions name no PL block were not applied here.

## (b) Checker results and every missing token with its justification
Command: python3 /tmp/claude-0/-home-user-megato/00d38b86-a9d4-564d-acaf-a8727e1b998d/scratchpad/enhance/check_invariants.py ORIGINAL ENHANCED

c1_1: size chars 31817 -> 48373 (+52.0%), est tokens 7954 -> 12093; strict_missing=0, soft_missing=17.
c2_1: size chars 33595 -> 50151 (+49.3%), est tokens 8399 -> 12538; strict_missing=0, soft_missing=17.
Both files have the same 17 soft tokens missing. All 17 are justified below, so unjustified = 0 for each file.

| Token | Category | Original line c1 / c2 | Justification |
|---|---|---|---|
| claim_id | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: it sits in the claims[] field list of the TP branch of GEMINI_4_ARGON_RESEARCH_ROLE_CONTRACT_V1. TP schemas are never assigned to GM campaign phases (design 3.17 "Removed (justified)"; ISSUE-25). |
| evidence_refs | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: same TP claims[] field list (3.17). |
| test_refs | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: same TP claims[] field list (3.17). |
| reviewed_claims | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP defects[]/reviewed_claims[] branch (3.17). |
| tp1_packet_hash | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP lineage-object branch (3.17). |
| tp2_packet_hash | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP lineage-object branch (3.17). |
| parent_claim_hashes | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP lineage-object branch (3.17). |
| resolved_defect_ids | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP3-schema sentence (3.17). |
| unresolved_defect_ids | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP3-schema sentence (3.17). |
| resolved_defects | soft snake_case | PL1:27 / PL2:27 | role-irrelevant: TP3-schema sentence (3.17). |
| HTS_BACKTEST_ANALYZE | soft upper_snake | PL1:127 / PL2:142 | role-irrelevant: the ANALYZE-only block label. Block map: "HTS_BACKTEST_ANALYZE / PL / (none) / removed (ANALYZE-only)" (ISSUE-06, ISSUE-25). Its PLAN-relevant rules remain: GM_PLAN_SEALED_TEXT_RULES_V1 RESOLUTION CONDITION (line 56: one Beta-settleable boolean, census/provenance criteria do not consume a cycle), CYCLE_IMPROVE (line 135: a rehash or provenance-only cycle is not a backtest), the PLAN phase line (73: from best_so_far toward binding_gate) and GM_PLAN_SELECTION_V1 Stall (65). |
| measured_scorecard | soft snake_case | PL1:130 / PL2:145 | role-irrelevant: ANALYZE response field of the removed HTS_BACKTEST_ANALYZE block. |
| gates_measured | soft snake_case | PL1:130 / PL2:145 | role-irrelevant: ANALYZE response field of the removed block. |
| failed_gates | soft snake_case | PL1:130 / PL2:145 | role-irrelevant: ANALYZE ledger field of the removed block. PLAN still reads "falsified formulas with failed gates" in the verbatim CONVERGENCE_V1 Memory line (143). |
| change_reason | soft snake_case | PL1:131 / PL2:146 | role-irrelevant: ANALYZE nomination field of the removed block (stall switch). |
| new_evidence | soft snake_case | PL1:131 / PL2:146 | role-irrelevant: ANALYZE nomination field of the removed block. |
| run_id | soft snake_case | PL1:115 / PL2:130 | role-irrelevant: it occurs only in the worker write path `agent_general_<role>/runtime/research/<run_id>/` of HOST_CONTROL_PLANE_OWNERSHIP. The GM_PLAN variant (3.9) drops the Workers sentences because GM writes no file. |

Expected vs actual: design 5.1 expects strict 0 (actual 0 in both files) and lists 18 expected soft tokens. economics_verdict is the one that is not missing: PRECEDENCE_V1 line 22 contains it ("economics_verdict follows the sealed decision_policy"). No label was renamed, so no "label renamed per block map" entry is needed.

## (c) Deviations from design.md
None. Every new block equals its design.md fence byte-for-byte (A5), and every verbatim or slot line equals the original line. These implementation choices stay within the design:
1. Format (section 0): every block is followed by exactly one blank line. This includes blocks that were contiguous in the original (quality block / ROLE_WORKFLOW=GM_PLAN; GEMINI contract / LEAN; GM_EXECUTION_RULES_V1 / TRANSPORT_NON_INTERACTIVE; HTS_BACKTEST_PROGRESS / CONVERGENCE_V1; read guide / INDEX_USE_RULE_V1; constants / MULTIPLE_TESTING_GUARD_V1), so "label line to next blank line" extracts exactly the design fence. The original triple blank line (PL1:161-163 / PL2:176-178) and blank line PL1:60 / PL2:73 inside the old task region are not reproduced.
2. The GM identity line stays attached to the header block, as original line 8 was. Every block therefore starts with a label line.
3. The two ASSIGNED_TASK ranges are joined without a blank line into one block whose first line is ASSIGNED_TASK.
4. The SELF-CHECK sentence is appended to PL:24 with a one-space separator.

## (d) Fidelity map: every original line that is not a whole line of the enhanced file
A script found these lines. c1: 8, 10, 24, 26, 27, 28, 44, 45, 46, 49, 50, 61, 62, 114, 115, 118, 119, 120, 122, 125, 127-131, 134, 149, 151. c2: 8, 10, 24, 26, 27, 28, 57, 58, 59, 62, 63, 74, 75, 129, 130, 133, 134, 135, 137, 140, 142-146, 149, 164, 166. Every other non-blank original line appears verbatim.

| Original c1 (c2) | Content | Disposition | Where the constraint lives now (enhanced line) |
|---|---|---|---|
| 8 (8) | identity line | consolidated: rewritten per 3.16 (role GM_PLAN -> "role": "gm" + "phase"; the fields that apply come from the schema) | 8 |
| 10 (10) | ASSIGNMENT FIRST | TP sentence removed (role-irrelevant: TP never assigned); the rest is verbatim | 25 |
| 24 (24) | SELF-CHECK | verbatim, with the 5.1 sentence appended | 40 |
| 26 (26) | "Do not edit next_goal.txt." | duplicate of CAMPAIGN | 125 |
| 27 (27) | GEMINI GM contract body | TP branches removed (role-irrelevant). Added: the sentence that Gamma runs the same model as GM, and the TOOLS pointer (3.17) | 72 |
| 28 (28) | PLAN and ANALYZE sentences | ANALYZE sentence removed (role-irrelevant); PLAN sentence reworded per 3.17 (legacy label ranked 5; GM never imports the toolkit) | 73 |
| 44 (57) | HTS_BACKTEST_PROGRESS label | GM variant label with its scope parenthesis (3.12) | 131 |
| 45 (58) | Flow line | moved into FLOW_POSITION_V1 line 3, which starts with the original sentence verbatim | 12 |
| 46 (59) | FINAL GOAL file is read-only: next_goal.txt path | consolidated into CAMPAIGN (same path) | 125 |
| 49 (62) | Label line | marked "(legacy default, PRECEDENCE_V1 rank 5)" | 134 |
| 50 (63) | CYCLE_IMPROVE | "Datum read/add is allowed." scoped: lane permission under DATUM; GM reads metadata only and plans no datum change | 135 |
| 51-59 (64-72) | CONVERGENCE_V1 | moved out of the task region unchanged | 137-145 |
| 61 (74) | "GM runs no core.quant_toolkit compute; read the sealed inputs only." | duplicate of read-guide line PL1:172 / PL2:188 (kept in the slot); the read-only scope is also in the FLOW role line and the overlay | 157/158; 13; 108; 122 |
| 62 (75) | GOAL rule | merged into the CAMPAIGN GM_PLAN variant (immutable FINAL GOAL; never edit or paste; gates/incumbent/allowed measurement/do-not list bind scope; this cycle_id only; GOAL_ACHIEVED/NEXT_PLAN/STOP/WAIT is a later GM_ANALYZE decision) | 124-129 |
| 114 (129) | Workers ICV line | role-irrelevant (worker-only); the GM ICV rules stay | 117-118 |
| 115 (130) | "If Host INPUT is valid, continue research." and the Workers write path | role-irrelevant; the "GM read-only: ..." sentences stay verbatim | 119 |
| 118-120, 122 (133-135, 137) | original CAMPAIGN_GOAL_DIRECTIVE | merged into the GM_PLAN variant. "author a new research_angle each cycle" becomes "choose research_angle by GM_PLAN_SELECTION_V1" (REQUIRED_RESEARCH_ANGLE first; "New" means absent from the used list; CYCLE_IMPROVE still forbids reuse). "Stay inside this cycle's RESEARCH_DIRECTIVE" becomes "write it for this cycle_id only ... do not write a future RESEARCH_DIRECTIVE". Line 121 (136) is verbatim. | 124-129; 66; 135 |
| 125 (140) | persona | GM_PLAN persona variant (3.15) | 151 |
| 127-131 (142-146) | HTS_BACKTEST_ANALYZE | removed (ANALYZE-only; see tokens in (b)). PLAN-relevant rules are kept in the lines named in (b). | 56, 65, 73, 135 |
| 134 (149) | OOS packet body | GM variant (3.14): lanes rehash and backtest; GM cites the Host-verified sorted_key_sha256 and hashes nothing | 148 |
| 149 (164) | third ICV wording | consolidated into HOST_CONTROL line 2 | 117 |
| 151 (166) | TARGET_FORMULA_REGISTRY absence | duplicate of the HOST_CONTROL "GM PLAN:" line | 118 |

## (e) Acceptance checks run (verify.py)
- A1 PASS: the c1_1 and c2_1 originals and the role table match their sha256.
- A2: the GM_PLAN names are identical. The full 10-file comparison waits for the other roles.
- A3 PASS: strict_missing 0 / 0; every soft token is justified in (b).
- A4 PASS: 60 lines differ between enhanced c1 and c2, and every one is a section 5.1 slot line of its own original.
- A5 PASS: every PL block equals its 3.x/5.1 fence byte-for-byte. The shared GM blocks (identity line, shared GEMINI line, GM_EXECUTION_RULES_V1, INDEX_USE_RULE_V1, MULTIPLE_TESTING_GUARD_V1, TRANSPORT_NON_INTERACTIVE, HTS GM variant, CONVERGENCE_V1, HOST_OOS GM variant) are the design texts, so they match AN when AN follows its fences.
- A6 PASS: the label order equals 5.1 steps 1-24, and PRECEDENCE_V1 directly follows FLOW_POSITION_V1.
- A7 PASS: no authoring-assistant model id. "Claude Opus" without a version appears only in the GEMINI contract line.
- A8 PASS: every number token in the enhanced files is a number token of an original or a role-table value.
- A9 PASS: every slot line is present as an exact whole line.
- A11 PASS: GM_PLAN_OUTPUT_SCHEMA_V1 appears once and is the last block.
- A12: +52.0% (c1_1) and +49.3% (c2_1), below the +60% flag.
- A14 PASS: "FALSIFIED when a gate misses" is absent from PL, "50%" is present, and "maximum available" is absent. Three lines outside slots contain "<= +0.15%". Line 134 says "legacy default" literally. Line 21 (PRECEDENCE_V1 rank 5, "Legacy HTS defaults") and line 39 (verbatim PL:23, "legacy HTS close-to-open campaign") mark the label as legacy in other words; both texts are fixed by the design (shared fence / verbatim line).
- A15 PASS: there are no Markdown headings outside the ASSIGNED_TASK slot, blocks are separated by exactly one blank line, no block contains a blank line, there is no trailing whitespace, and each file ends with a single LF.

## (f) README items and observations (no text changed)
KEEP_AS_IS_WITH_REASON (ISSUE-69 and ISSUE-70) items visible in GM_PLAN, all kept verbatim:
- The c2 index (enhanced c2 line 157) has truncated display ids "I2_WF_MINUTE_OVLP_1519_H02_UPLOW_PLUS_RANGELOW_VWAP_ABSORPTION_WICKGUARD_EQ20_ME" and "..._UPNORM_VWAP_PULLBACK_WICKGUARD_EQ20_MEANLO" (their pointers carry the full ids). It also has the non-candidate rows variant_A_ddof0_test_i2 and variant_B_ddof1_test_i2, and duplicate I0 rows (BETA scorecard /0 and /3; GAMMA scorecard /0 and /5). INDEX_USE_RULE_V1 makes these safe.
- MULTIPLE_TESTING_CONSTANTS_V1 states z only for M_cum 18, while PL2:44 names M_cum=19. MULTIPLE_TESTING_GUARD_V1 makes the adjusted bound UNKNOWN and names the missing constant.
- The c2 Beta resolution_condition (PL2:43) contains alpha_beta_* conjuncts and unbound challenger_* terms. Handled by the RESOLUTION CONDITION rule.
- PL2:52 says "write bottleneck_verification in BETA_LANE_RESULT.json". Handled by the BETA FILE rule.
- PL2:51 and PL2:53 repeat ANALYZE mapping and resolution lines (auditor removal proposal rejected: Host slot).
- PL2:44 maps decidable_claim outcomes (e.g. "INCONCLUSIVE -> retain HOLD_FOR_EVIDENCE") differently from the sealed branches PL2:46-48. Handled by the BRANCHES rule.
- "Gemini 4 Argon High has a 65,536 per-call output token limit." is unverified (ISSUE-70).

Observations for the verify step (residual wording risks in design-fixed text; left unchanged because the design fences are binding and A5 requires byte equality):
1. The FLOW_POSITION_V1 GM_PLAN role line says "GM runs, measures, spawns and writes nothing.", while GM_EXECUTION_RULES_V1 TOOLS (line 82) allows read-only run_command extraction for JSON over 50 KB. The intended reading is "runs no lane work". The read-guide extraction instruction is Host-injected slot text (rank 2), and TOOLS is the specific rule, so PRECEDENCE_V1 settles the conflict in favour of the extraction.
2. GM_PLAN_SPEC_RULES_V1 EXPLORATION (line 45) puts the target_hypothesis id "in the lane instructions", while GAMMA RECIPES (line 49) and sealed line PL1:104 / PL2:118 forbid candidate or survivor IDs for Gamma. For gamma.instruction, the rank-2 sealed line and GAMMA RECIPES ("stricter than any example in this prompt") prevail; Gamma reads the ids from its sealed contract copy.
