# ledger_GM_ANALYZE (assembled by build_an.py from DESIGN.md 5.2 section order)

Design conformance: all 7 section-5.2 fences and all section-3 variants for GM_ANALYZE are present verbatim; Host-injected lines AN:1-7, 14-15, 19-25 (last sentence of AN:22 removed per spec), 30-32, 33-44, 45-58, 60-79, 150-152, 154-159, 161-164 copied verbatim from the c1/c2 original.
acceptance.py: strict_missing = 0; A4, A5, A7, A8, A15 pass.

Soft-missing tokens and justification:
- claim_id, evidence_refs, test_refs, reviewed_claims, parent_claim_hashes, tp1_packet_hash, tp2_packet_hash, resolved_defect_ids, unresolved_defect_ids, resolved_defects: TP-mode branches of the GEMINI GM contract; TP schemas are never assigned to GM campaign phases (DESIGN.md 3.17).
- FIRST_RUN_GM_ORDER, progress_review: PLAN persona text (AN:116-117), replaced by the ANALYZE persona (DESIGN.md 3.15).
- run_id: worker-only sentence of HOST_CONTROL_PLANE_OWNERSHIP (AN:86), role-irrelevant (DESIGN.md 3.9 GM_ANALYZE variant).
