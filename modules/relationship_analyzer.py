def analyze_relationship(text):
    """
    Heard AI Relationship Analyzer v1
    """

    text = text.lower()

    findings = []

    # İlgi dengesizliği
    if "hep ben" in text or "sadece ben" in text:
        findings.append("one_sided_effort")

    # Belirsizlik
    if "kararsız" in text or "bilmiyorum dedi" in text:
        findings.append("mixed_signals")

    # Sürekli kaybolup gelme
    if "geri döndü" in text or "tekrar yazdı" in text:
        findings.append("push_pull")

    # Görmezden gelme
    if "cevap vermedi" in text or "görüldü attı" in text:
        findings.append("lack_of_response")

    # Öz değer riski
    if "kendimi değersiz" in text:
        findings.append("self_worth_risk")

    return findings