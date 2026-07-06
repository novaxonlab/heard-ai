def analyze_relationship(text):
    """
    Heard AI Relationship Analyzer v2

    Detects relationship dynamics instead of only keywords.
    """

    text = text.lower()

    findings = []

    # -------------------------
    # One-sided effort
    # -------------------------

    if any(x in text for x in [
        "hep ben",
        "sadece ben",
        "ilk ben yazıyorum",
        "ben uğraşıyorum",
        "çabayı ben gösteriyorum"
    ]):
        findings.append("one_sided_effort")

    # -------------------------
    # Mixed signals
    # -------------------------

    if any(x in text for x in [
        "kararsız",
        "bilmiyorum dedi",
        "emin değil",
        "bir öyle bir böyle",
        "bazen çok ilgili"
    ]):
        findings.append("mixed_signals")

    # -------------------------
    # Push & Pull
    # -------------------------

    if any(x in text for x in [
        "geri döndü",
        "tekrar yazdı",
        "bir gidiyor bir geliyor",
        "kayboluyor",
        "haftalar sonra yazdı"
    ]):
        findings.append("push_pull")

    # -------------------------
    # Lack of response
    # -------------------------

    if any(x in text for x in [
        "cevap vermedi",
        "görüldü attı",
        "mesajıma dönmedi",
        "yazmadı",
        "beni bekletiyor"
    ]):
        findings.append("lack_of_response")

    # -------------------------
    # Self-worth risk
    # -------------------------

    if any(x in text for x in [
        "kendimi değersiz",
        "beni istemiyor galiba",
        "yeterli değilim",
        "beni seçmedi"
    ]):
        findings.append("self_worth_risk")

    # -------------------------
    # Breadcrumbing
    # -------------------------

    if any(x in text for x in [
        "arada yazıyor",
        "canı isteyince yazıyor",
        "kaybolup geri geliyor",
        "sadece storyme bakıyor"
    ]):
        findings.append("possible_breadcrumbing")

    # -------------------------
    # Love bombing
    # -------------------------

    if any(x in text for x in [
        "ilk başta çok ilgiliydi",
        "bir anda değişti",
        "başta mükemmeldi"
    ]):
        findings.append("possible_love_bombing")

    # -------------------------
    # Gaslighting
    # -------------------------

    if any(x in text for x in [
        "her şeyi bana yüklüyor",
        "beni suçluyor",
        "abartıyorsun dedi",
        "hayal görüyorsun dedi"
    ]):
        findings.append("possible_gaslighting")

    return findings