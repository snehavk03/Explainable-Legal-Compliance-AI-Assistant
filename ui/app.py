import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.preprocess import split_into_clauses
from src.classification.clause_classifier import ClauseClassifier
from src.retrieval.precedent_retriever import PrecedentRetriever
from src.compliance.compliance_checker import ComplianceChecker
from src.reasoning.explainable_reasoner import ExplainableReasoner

st.title("Explainable Legal Compliance Assistant 🧑‍⚖️")
uploaded = st.file_uploader("Upload Contract (.txt)", type=["txt"])
if uploaded:
    text = uploaded.read().decode("utf-8")
    clauses = split_into_clauses(text)
    classifier, retriever, checker, reasoner = ClauseClassifier(), PrecedentRetriever(), ComplianceChecker(), ExplainableReasoner()
    retriever.build_index(["XYZ Pvt vs Emp (2019): unfair termination","ABC Corp vs Contractor (2021): one-sided clause"])
    for c in clauses:
        st.write(f"**Clause:** {c}")
        t="termination" if "terminate" in c.lower() else "confidentiality"
        law=checker.check(t)
        precedents=retriever.search(c)
        reason=reasoner.generate_reason(c,law)
        st.write(f"- **Type:** {t}\n- **Law:** {law}\n- **Cases:** {precedents}\n- **Explanation:** {reason}")
        st.markdown('---')