class ExplainableReasoner:
    def generate_reason(self,clause,law):
        return f"The clause '{clause[:50]}...' is analyzed under {law} because it impacts fairness or legality."
if __name__=="__main__":
    print(ExplainableReasoner().generate_reason('Termination clause','Section 23, Indian Contract Act'))