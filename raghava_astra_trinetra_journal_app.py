import streamlit as st
import pandas as pd
import json
from datetime import datetime, date

# ==============================================================================
# 🏹 RAGHAVA ASTRA • TRINETRA AI — MASTER WEALTH, TRADING & AI-CA DOCK
# (DESIGN #6 + DESIGN #9 MULTI-COLOR FUSION • STANDALONE JOURNAL APP)
# "Trinetra Sees the Truth. Raghava Locks the Strike."
# ==============================================================================
st.set_page_config(
    page_title="RAGHAVA ASTRA • TRINETRA AI — Master Wealth, Trading & AI-CA Dock",
    page_icon="🏹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=IBM+Plex+Mono:wght@600;700&display=swap');
.stApp {
    background: radial-gradient(circle at 15% 0%, rgba(139, 92, 246, 0.16) 0%, transparent 40%),
                radial-gradient(circle at 85% 5%, rgba(6, 182, 212, 0.15) 0%, transparent 42%),
                #050811 !important;
    color: #f8fafc !important;
    font-family: 'Inter', sans-serif !important;
}
.bento-card {
    background: linear-gradient(160deg, rgba(17, 25, 44, 0.94) 0%, rgba(9, 14, 26, 0.98) 100%);
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 12px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.65);
}
.bento-emerald { border: 1.6px solid rgba(16, 185, 129, 0.55); }
.bento-cyan    { border: 1.6px solid rgba(6, 182, 212, 0.55); }
.bento-violet  { border: 1.8px solid rgba(139, 92, 246, 0.65); background: linear-gradient(155deg, rgba(88, 28, 135, 0.32) 0%, rgba(15, 23, 42, 0.96) 55%, rgba(8, 51, 68, 0.32) 100%); }
.bento-coral   { border: 1.6px solid rgba(244, 63, 94, 0.55); }
.bento-amber   { border: 1.6px solid rgba(245, 158, 11, 0.55); }
.mono-num      { font-family: 'IBM Plex Mono', monospace; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# INITIALIZE SESSION STATE (DEFAULT INDIAN FAMILY + TRADER DATASET)
# ------------------------------------------------------------------------------
if "recurring_bills" not in st.session_state:
    st.session_state.recurring_bills = [
        {"id": "b1", "title": "Wi-Fi / Broadband (Trading Setup)", "amount": 899, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 37 Utility"},
        {"id": "b2", "title": "Mobile Data & Recharge", "amount": 449, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 37 Comm."},
        {"id": "b3", "title": "TradingView Pro & Market Data Feed", "amount": 1499, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 37 Software"},
        {"id": "b4", "title": "Brokerage, STT (0.15%) & Exchange Fees", "amount": 2450, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 37 Direct"},
        {"id": "b5", "title": "iPad & Laptop Depreciation (Monthly Share)", "amount": 1800, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 32 Deprec."},
        {"id": "b6", "title": "Home-Office Electricity Share (25%)", "amount": 800, "category": "ITR-3 Business Deduct", "active": True, "code": "Sec 37 Power"},
        {"id": "b7", "title": "Kirana, Ration & Cold-Pressed Multigrain Atta", "amount": 6500, "category": "Bandhe Ghar Fixed", "active": True, "code": "Ghar Need"},
        {"id": "b8", "title": "Monthly Doodh & Dairy Hisab", "amount": 2400, "category": "Bandhe Ghar Fixed", "active": True, "code": "Ghar Need"},
        {"id": "b9", "title": "Ghar Bijli Bill (75%) & LPG Cylinder", "amount": 2600, "category": "Bandhe Ghar Fixed", "active": True, "code": "Ghar Need"},
        {"id": "b10", "title": "Daughter (Roshni) & Family Care / Education", "amount": 3000, "category": "Bandhe Ghar Fixed", "active": True, "code": "Family Care"},
        {"id": "b11", "title": "80C Equity/Index SIP & Sukanya Samriddhi", "amount": 15000, "category": "SIP & 80C/80D Wealth", "active": True, "code": "Sec 80C"},
        {"id": "b12", "title": "Family Health Insurance (Mediclaim Monthly)", "amount": 2500, "category": "SIP & 80C/80D Wealth", "active": True, "code": "Sec 80D"},
    ]

if "trades" not in st.session_state:
    st.session_state.trades = [
        {"date": "2026-11-11", "strike": "NIFTY 25000 CE", "pnl": 18500, "why": "3-Lock + 7-EMA Root", "sl_type": "Target Hit (T1/T2/T3)", "greed": "Disciplined Trail (Zero Greed)", "note": "Gap-up breakout + 7-EMA root pullback T3 hit."},
        {"date": "2026-11-12", "strike": "NIFTY 25300 PE", "pnl": 16200, "why": "3-Lock + 7-EMA Root", "sl_type": "Target Hit (T1/T2/T3)", "greed": "Disciplined Trail (Zero Greed)", "note": "Supply rejection breakdown below Purple Box neckline."},
        {"date": "2026-11-12", "strike": "NIFTY 25250 CE", "pnl": -2200, "why": "Sideways Mid-Box Guess", "sl_type": "Bad Mistake SL", "greed": "Quota Greed (Overtraded)", "note": "Took mid-box trade after morning win; avoidable Bad SL."},
        {"date": "2026-11-13", "strike": "NIFTY 25150 CE", "pnl": 9200, "why": "3-Lock + 7-EMA Root", "sl_type": "Target Hit (T1/T2/T3)", "greed": "Disciplined Trail (Zero Greed)", "note": "09:30 AM Purple Box reclaim T2 locked."},
        {"date": "2026-11-13", "strike": "NIFTY 25200 PE", "pnl": -1500, "why": "3-Lock + 7-EMA Root", "sl_type": "Good System SL", "greed": "Disciplined Trail (Zero Greed)", "note": "Followed system rule; small 10-pt system SL respected."},
        {"date": "2026-11-13", "strike": "NIFTY 25100 CE", "pnl": 8000, "why": "Wyckoff Spring Reclaim", "sl_type": "Target Hit (T1/T2/T3)", "greed": "Disciplined Trail (Zero Greed)", "note": "02:35 PM Wyckoff Spring reclaim captured cleanly."},
    ]

if "expenses" not in st.session_state:
    st.session_state.expenses = [
        {"date": "2026-11-10", "title": "Taaza Sabzi & Fruits (Weekly Mandi)", "amount": 1450, "category": "Rozmarra Essential"},
        {"date": "2026-11-11", "title": "Scooter & Car Petrol Refill", "amount": 1850, "category": "Rozmarra Essential"},
        {"date": "2026-11-12", "title": "Family Pharmacy & Vitamins", "amount": 900, "category": "Rozmarra Essential"},
        {"date": "2026-11-13", "title": "Chhath / Kartik Parv & Shagun Buffer", "amount": 2500, "category": "Tyohar & Emergency"},
        {"date": "2026-11-14", "title": "Late-Night Zomato & Flash Sale Gadget", "amount": 1850, "category": "Fizul Kharch"},
        {"date": "2026-11-15", "title": "Morning Sabzi & Khula Doodh/Paneer", "amount": 1000, "category": "Rozmarra Essential"},
    ]


# ------------------------------------------------------------------------------
# 🌅 CHITRAGUPTA SANDHYA 7-8 PM HINGLISH NLU PARSER & AUTO-CLASSIFIER (PYTHON)
# ------------------------------------------------------------------------------
import re

DIARY_SAMPLES_PY = {
    "Sample 1: +₹4,800 Win, -₹1,500 Bad SL, Sabzi, Petrol, Wi-Fi & Zomato": (
        "Aaj subah 9:25 pe Nifty 25150 CE me 3-lock 7-EMA root pe trade liya aur T2 trail karke 4800 profit book kiya, "
        "par dopahar 1 baje sideways box me lalach me 25200 PE le liya jisme 1500 ka galat SL kat gaya. "
        "Shaam ko mandi se 220 ki sabzi aur phal laya, scooty me 300 ka petrol dalwaya, trading setup ka 899 wala Wi-Fi recharge kiya, "
        "aur raat ko Zomato se 380 ka pizza mangwa liya. Subah 45 min workout kiya aur Raghava Astra V21 test kiya."
    ),
    "Sample 2: 2 Sniper Wins (+₹11,200), Good SL (-₹1,100), Dawai, SIP & Workout": (
        "Aaj discipline ke saath subah Nifty 25100 CE me 3-lock setup par 6400 ka profit book kiya, "
        "phir 11:20 pe 25250 PE me Wyckoff spring reclaim par 4800 profit mila, aur ek trade me 1100 ka chhota system SL rule follow karke kata. "
        "Ghar ke liye 450 ki dawai aur medical vitamin laya, 180 ka doodh aur paneer laya, aur 15000 ki monthly 80C Nifty Index SIP auto-debit hui. "
        "Sham ko papa ke saath walk pe gaya."
    ),
    "Sample 3: Multi-Item Mandi, Shagun ₹501, TradingView Bill & Parivar Time": (
        "Aaj market sideways tha isliye zero overtrading ki aur sirf 1 sniper trade Nifty 25200 CE me 3-lock par 3900 profit leke terminal band kar diya. "
        "Mandi me 140 ki hari sabzi, 110 ke phal, 260 ka petrol dalwaya, parivar me 501 rupaye shagun gift diya, "
        "aur 1499 ka TradingView Pro subscription pay kiya. Raat ko 1 ghanta Python backtest code likha."
    ),
}


if "base_capital" not in st.session_state:
    st.session_state.base_capital = 100000
if "bank_payout_locked" not in st.session_state:
    st.session_state.bank_payout_locked = 28000
if "patience_days" not in st.session_state:
    st.session_state.patience_days = 2
if "udhaari_list" not in st.session_state:
    st.session_state.udhaari_list = [
        {"id": "u1", "person": "Vikram (Fuel & Highway Toll Split)", "amount": 1500, "type": "Vasoolna Hai (Lent)", "settled": False, "date": "2026-11-11"},
        {"id": "u2", "person": "Aman (Evening Cafe & Snacks)", "amount": 600, "type": "Vasoolna Hai (Lent)", "settled": False, "date": "2026-11-14"},
    ]
if "reconcile_data" not in st.session_state:
    st.session_state.reconcile_data = {
        "broker_gross_pnl": 54600,
        "broker_charges": 6400,
        "broker_net_pnl": 48200,
        "broker_trade_count": 8,
        "bank_total_upi_debits": 24850,
        "bank_chillar_count": 38,
        "bank_chillar_amount": 1940,
    }

if "diary_logs" not in st.session_state:
    st.session_state.diary_logs = [
        {
            "date": "2026-11-13",
            "raw_text": "Subah 09:30 pe 25150 CE me +9200 aur 02:35 PM Wyckoff Spring me +8000 book kiya. Sham ko Chhath puja shagun 2500 diya aur 45 min walk kiya.",
            "activities": ["💪 Health: 45 min walk kiya", "👨‍👩‍👧 Parivar: Chhath puja shagun"],
            "summary_badge": "2 Wins (+₹17,200) • 1 Tyohar Expense (₹2,500)"
        }
    ]

if "habits" not in st.session_state:
    st.session_state.habits = [
        {"rule": "1. Waited for 3-Lock + 7-EMA Root", "days": [1]*11 + [0] + [1]*3},
        {"rule": "2. Zero Sideways Mid-Box Trade", "days": [1]*11 + [0] + [1]*3},
        {"rule": "3. Respected Pre-Defined Smart SL", "days": [1]*15},
        {"rule": "4. Zero Greed Overtrading After T2/T3", "days": [1]*11 + [0] + [1]*3},
        {"rule": "5. Logged Daily Rozmarra Kharch", "days": [1]*15},
        {"rule": "6. Zero Fizul Impulse Spending", "days": [1]*4 + [0] + [1]*8 + [0, 1]},
    ]


def _extract_non_strike_amounts(s: str):
    cleaned = re.sub(r"\b\d{1,2}:\d{2}\b", " ", str(s or ""))
    cleaned = re.sub(r"\b\d{1,2}\s*(?:baje|am|pm|min|minute|ghanta|hr|hours|din|lock|ema|sniper)\b", " ", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\b(?:3-lock|7-ema|80c|80d|itr-3|sec\s*\d+|v\d+)\b", " ", cleaned, flags=re.IGNORECASE)
    stk_m = (
        re.search(r"\b(nifty|banknifty|sensex|finnifty)?\s*(\d{5})\s*(ce|pe|call|put)\b", s, flags=re.IGNORECASE)
        or re.search(r"\b(nifty|banknifty|sensex|finnifty)\s*(\d{5})\b", s, flags=re.IGNORECASE)
    )
    stk_num = stk_m.group(2) if stk_m else None
    amounts = []
    for m in re.finditer(r"(?:₹|rs\.?\s*)?(\d+(?:,\d{3})*(?:\.\d+)?)(\s*k)?\b", cleaned, flags=re.IGNORECASE):
        val = float(m.group(1).replace(",", ""))
        if m.group(2) and m.group(2).strip().lower() == "k":
            val *= 1000.0
        rounded = int(round(val))
        if stk_num and str(rounded) == stk_num:
            continue
        if rounded >= 10:
            amounts.append(rounded)
    return amounts, stk_m


def parse_sandhya_diary_text(raw_text: str, entry_date: str, recurring_bills: list, enable_bandhe_dedup: bool = True) -> dict:
    text = str(raw_text or "").strip()
    if not text:
        return {"trades": [], "expenses": [], "activities": [], "habit_updates": [1, 1, 1, 1, 1, 1]}

    raw_sentences = re.split(r"(?:[.;!\n]+|,\s*par\s+|\s+(?:lekin|magar|phir|uske baad)\s+)", text, flags=re.IGNORECASE)
    clauses = []
    for sent in raw_sentences:
        s = sent.strip()
        if not s:
            continue
        sub_parts = re.split(r"(?:,\s*|\s+aur\s+)", s, flags=re.IGNORECASE)
        buf = ""
        for part in sub_parts:
            p = part.strip()
            if not p:
                continue
            p_amts, _ = _extract_non_strike_amounts(p)
            buf_amts, _ = _extract_non_strike_amounts(buf)
            is_act = bool(re.search(r"(workout|walk|gym|yoga|code|test|study|papa|mummy|sleep|meditat)", p, flags=re.IGNORECASE)) and not p_amts
            if buf and ((p_amts and buf_amts) or (is_act and not buf_amts)):
                clauses.append(buf.strip())
                buf = p
            else:
                buf = f"{buf} aur {p}" if buf else p
        if buf.strip():
            clauses.append(buf.strip())

    trades = []
    expenses = []
    activities = []

    for clause in clauses:
        c_low = clause.lower()
        amounts, stk_m = _extract_non_strike_amounts(clause)

        strike = ""
        if stk_m:
            idx_name = (stk_m.group(1) or "NIFTY").upper()
            stk_num = stk_m.group(2)
            opt_t = (stk_m.group(3) or "").upper() if stk_m.lastindex and stk_m.lastindex >= 3 else ""
            if opt_t == "CALL":
                opt_t = "CE"
            elif opt_t == "PUT":
                opt_t = "PE"
            if not opt_t:
                opt_t = "PE" if re.search(r"\b(pe|put)\b", clause, flags=re.IGNORECASE) else "CE"
            strike = f"{idx_name} {stk_num} {opt_t}"
        elif re.search(r"\b(nifty|banknifty|sensex)\b", clause, flags=re.IGNORECASE) and re.search(r"\b(ce|pe|call|put)\b", clause, flags=re.IGNORECASE):
            is_pe = bool(re.search(r"\b(pe|put)\b", clause, flags=re.IGNORECASE))
            strike = f"NIFTY ATM {'PE' if is_pe else 'CE'}"

        is_trade_cue = (
            bool(re.search(r"\b(trade|profit|loss|sl|stoploss|stop\s*loss|target|t1|t2|t3|3-lock|7-ema|wyckoff|spring|sniper|intraday|ce|pe|call|put|book\s*kiya|kat\s*gaya)\b", c_low))
            and not bool(re.search(r"\b(tradingview|setup\s*ka|wifi|wi-fi|recharge|subscription|sip)\b", c_low))
        )

        if is_trade_cue and amounts:
            amt = amounts[-1]
            is_loss = bool(re.search(r"\b(loss|sl|stoploss|stop\s*loss|kat\s*gaya|kata|chala\s*gaya|nuksan|minus)\b", c_low)) and not bool(re.search(r"\b(zero\s*sl|no\s*sl)\b", c_low))
            pnl = -abs(amt) if is_loss else abs(amt)

            why = "3-Lock + 7-EMA Root"
            if re.search(r"(spring|wyckoff|reclaim|shakeout)", c_low):
                why = "Wyckoff Spring Reclaim"
            elif re.search(r"(3-lock|7-ema|sniper|srb)", c_low):
                why = "3-Lock + 7-EMA Root"
            elif re.search(r"(sideways|mid-box|box\s*ke\s*beech|box\s*me|range|chop)", c_low):
                why = "Sideways Mid-Box Guess"
            elif re.search(r"(fomo|running\s*candle|bhagte|top\s*chase|chase)", c_low):
                why = "Running Candle FOMO"
            elif re.search(r"(revenge|gusse|turant\s*baad|cover\s*karne)", c_low):
                why = "Revenge Trade"

            sl_type = "Target Hit (T1/T2/T3)"
            if pnl < 0:
                if re.search(r"(galat|bad|mistake|lalach|fomo|sideways|box|revenge|rule\s*toda|bina\s*setup)", c_low) or why in ("Sideways Mid-Box Guess", "Running Candle FOMO", "Revenge Trade"):
                    sl_type = "Bad Mistake SL"
                else:
                    sl_type = "Good System SL"

            greed = "Disciplined Trail (Zero Greed)"
            if re.search(r"(overtrade|overtrading|lalach|quota|bar\s*bar|sideways|revenge)", c_low) and pnl < 0:
                greed = "Quota Greed (Overtraded)"
            elif re.search(r"(trail\s*nahi|wapas\s*loss|target\s*greed)", c_low):
                greed = "Target Greed (Didn't Trail)"

            trades.append({
                "date": entry_date,
                "strike": strike or "NIFTY 25150 CE",
                "pnl": pnl,
                "why": why,
                "sl_type": sl_type,
                "greed": greed,
                "note": clause.strip()
            })
            continue

        if amounts:
            amt = amounts[0]
            category = "Rozmarra Essential"
            clean_title = "Rozmarra Grihasthi Item"
            bandha_kw = ""

            if re.search(r"(wifi|wi-fi|broadband|internet|airtel|jio\s*fiber)", c_low):
                category = "ITR-3 Business Deduct"
                clean_title = "Wi-Fi / Broadband (Trading Setup)"
                bandha_kw = "wi-fi"
            elif re.search(r"(mobile\s*data|mobile\s*recharge|sim\s*recharge|data\s*pack)", c_low):
                category = "ITR-3 Business Deduct"
                clean_title = "Mobile Data & Recharge"
                bandha_kw = "mobile data"
            elif re.search(r"(tradingview|market\s*data|sensibull|opstra|chartink)", c_low):
                category = "ITR-3 Business Deduct"
                clean_title = "TradingView Pro & Market Data Feed"
                bandha_kw = "tradingview"
            elif re.search(r"(brokerage|stt|exchange\s*fee)", c_low):
                category = "ITR-3 Business Deduct"
                clean_title = "Brokerage, STT & Exchange Fees"
                bandha_kw = "brokerage"
            elif re.search(r"(ipad|laptop|macbook|monitor|ups|keyboard|mouse)", c_low):
                category = "ITR-3 Business Deduct"
                clean_title = "Trading Hardware / Tech Accessory"
            elif re.search(r"(sip|index\s*fund|mutual\s*fund|sukanya|ppf|elss|nps|80c)", c_low):
                category = "SIP & 80C/80D Wealth"
                clean_title = "80C Equity/Index SIP & Sukanya"
                bandha_kw = "80c"
            elif re.search(r"(mediclaim|health\s*insurance|lic|term\s*plan|80d)", c_low):
                category = "SIP & 80C/80D Wealth"
                clean_title = "Family Health Insurance (Mediclaim)"
                bandha_kw = "insurance"
            elif re.search(r"(zomato|swiggy|pizza|burger|junk|momos|cold\s*drink|party|faltu|fizul|impulse|flash\s*sale)", c_low):
                category = "Fizul Kharch"
                clean_title = "Zomato / Pizza (Fizul Order)" if "pizza" in c_low else "Zomato / Swiggy Impulse Spend"
            elif re.search(r"(tyohar|puja|shagun|gift|diwali|holi|chhath|rakhi|mehman|shadi|yatra|emergency)", c_low):
                category = "Tyohar & Emergency"
                clean_title = "Parivar Shagun / Gift" if re.search(r"(shagun|gift)", c_low) else "Tyohar & Puja Buffer"
            else:
                category = "Rozmarra Essential"
                if re.search(r"(sabzi|phal|fruit|mandi|vegetable)", c_low):
                    clean_title = "Taaza Sabzi & Phal (Mandi)"
                elif re.search(r"(petrol|diesel|fuel|scooty|scooter|car|cng)", c_low):
                    clean_title = "Petrol / Vehicle Fuel"
                elif re.search(r"(dawai|medicine|medical|pharmacy|vitamin|doctor)", c_low):
                    clean_title = "Family Medical & Pharmacy"
                elif re.search(r"(doodh|paneer|dairy|curd|dahi)", c_low):
                    clean_title = "Doodh & Dairy"
                    if re.search(r"(monthly|mahine)", c_low):
                        bandha_kw = "doodh"
                elif re.search(r"(kirana|ration|atta|dal|oil)", c_low):
                    clean_title = "Kirana & Ghar Ration"
                    if re.search(r"(monthly|mahine)", c_low):
                        bandha_kw = "kirana"
                else:
                    clean_title = "Rozmarra Ghar Kharch"

            matched_bandha = None
            if enable_bandhe_dedup and bandha_kw:
                for b in recurring_bills:
                    if b.get("active") and bandha_kw in b.get("title", "").lower():
                        matched_bandha = b
                        break

            expenses.append({
                "date": entry_date,
                "title": clean_title,
                "amount": amt,
                "category": category,
                "matched_bandha_id": matched_bandha["id"] if matched_bandha else None,
                "matched_bandha_title": matched_bandha["title"] if matched_bandha else None,
            })
            continue

        if len(clause) >= 6:
            tag = "📖 Dinacharya"
            if re.search(r"(workout|walk|gym|run|yoga|exercise|health)", c_low):
                tag = "💪 Health"
            elif re.search(r"(code|python|raghava|astra|trinetra|backtest|test|chart|study)", c_low):
                tag = "💻 Quant R&D"
            elif re.search(r"(papa|mummy|roshni|parivar|family|temple|mandir|puja)", c_low):
                tag = "👨‍👩‍👧 Parivar"
            activities.append(f"{tag}: {clause.strip()}")

    has_bad_why = any(t["why"] in ("Sideways Mid-Box Guess", "Running Candle FOMO", "Revenge Trade") for t in trades)
    has_mid_box = any(t["why"] == "Sideways Mid-Box Guess" for t in trades)
    has_bad_sl = any(t["sl_type"] == "Bad Mistake SL" for t in trades)
    has_greed = any(t["greed"] != "Disciplined Trail (Zero Greed)" for t in trades)
    logged_diary = (len(trades) + len(expenses) + len(activities)) > 0
    has_fizul = any(e["category"] == "Fizul Kharch" for e in expenses)

    habit_updates = [
        0 if has_bad_why else 1,
        0 if has_mid_box else 1,
        0 if has_bad_sl else 1,
        0 if has_greed else 1,
        1 if logged_diary else 0,
        0 if has_fizul else 1,
    ]
    return {"trades": trades, "expenses": expenses, "activities": activities, "habit_updates": habit_updates}

# ------------------------------------------------------------------------------
# COMPUTE LIVE AI-CA & ITR-3 METRICS
# ------------------------------------------------------------------------------
sec37_auto = sum(b["amount"] for b in st.session_state.recurring_bills if b["active"] and b["category"] == "ITR-3 Business Deduct")
bandhe_ghar = sum(b["amount"] for b in st.session_state.recurring_bills if b["active"] and b["category"] == "Bandhe Ghar Fixed")
sip_80c = sum(b["amount"] for b in st.session_state.recurring_bills if b["active"] and b["category"] == "SIP & 80C/80D Wealth")

rozmarra = sum(e["amount"] for e in st.session_state.expenses if e["category"] == "Rozmarra Essential")
sec37_manual = sum(e["amount"] for e in st.session_state.expenses if e["category"] == "ITR-3 Business Deduct")
tyohar = sum(e["amount"] for e in st.session_state.expenses if e["category"] == "Tyohar & Emergency")
fizul = sum(e["amount"] for e in st.session_state.expenses if e["category"] == "Fizul Kharch")

gross_win = sum(t["pnl"] for t in st.session_state.trades if t["pnl"] >= 0)
good_sl = sum(abs(t["pnl"]) for t in st.session_state.trades if t["pnl"] < 0 and t["sl_type"] != "Bad Mistake SL")
bad_sl = sum(abs(t["pnl"]) for t in st.session_state.trades if t["pnl"] < 0 and t["sl_type"] == "Bad Mistake SL")
net_pnl = gross_win - good_sl - bad_sl
wins_cnt = sum(1 for t in st.session_state.trades if t["pnl"] >= 0)
win_rate = round((wins_cnt / len(st.session_state.trades)) * 100) if st.session_state.trades else 100

total_sec37 = sec37_auto + sec37_manual
total_grihasthi = bandhe_ghar + rozmarra
total_leakage = fizul + bad_sl
net_taxable_fo = max(0, net_pnl - total_sec37)
monthly_turnover = round((gross_win + good_sl + bad_sl) * 2.8)

# ------------------------------------------------------------------------------
# HEADER & TOP 4 MULTI-COLOR KPI CARDS (DESIGN #9)
# ------------------------------------------------------------------------------
st.markdown("""
<div class="bento-card" style="border: 1.5px solid #334155;">
  <h2 style="margin:0; background: linear-gradient(90deg, #fff, #67e8f9, #6ee7b7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    🏹 RAGHAVA ASTRA • TRINETRA AI — MASTER WEALTH, TRADING & AI-CA DOCK
  </h2>
  <p style="margin:4px 0 0 0; font-size:0.85rem; color:#94a3b8;">
    "Trinetra Sees the Truth. Raghava Locks the Strike." • Design #6 (1st-of-Month Auto-Tagged Bills) + Design #9 (5-Tab Multi-Color Bento Dock)
  </p>
</div>
""", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""
    <div class="bento-card bento-emerald">
      <div style="font-size:0.72rem; font-weight:800; color:#34d399;">1. MONTHLY NET TRADING P&L</div>
      <div class="mono-num" style="font-size:1.65rem; color:#6ee7b7;">+₹{net_pnl:,}</div>
      <div style="font-size:0.75rem; color:#cbd5e1;">Win Rate: <b>{win_rate}%</b> • Sec 43(5) Business</div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown(f"""
    <div class="bento-card bento-cyan">
      <div style="font-size:0.72rem; font-weight:800; color:#22d3ee;">2. GHAR-GRIHASTHI & FAMILY</div>
      <div class="mono-num" style="font-size:1.65rem; color:#67e8f9;">₹{total_grihasthi:,}</div>
      <div style="font-size:0.75rem; color:#cbd5e1;">Bandhe: ₹{bandhe_ghar:,} + Rozmarra: ₹{rozmarra:,}</div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown(f"""
    <div class="bento-card bento-violet">
      <div style="font-size:0.72rem; font-weight:800; color:#c084fc;">3. AUTO-TAGGED ITR-3 & 80C/D</div>
      <div class="mono-num" style="font-size:1.65rem; color:#d8b4fe;">₹{total_sec37 + sip_80c:,}</div>
      <div style="font-size:0.75rem; color:#cbd5e1;">Sec 37 Business: <b>₹{total_sec37:,}</b> + 80C/D: ₹{sip_80c:,}</div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown(f"""
    <div class="bento-card bento-coral">
      <div style="font-size:0.72rem; font-weight:800; color:#fb7185;">4. FIZUL KHARCH + BAD SL LEAKAGE</div>
      <div class="mono-num" style="font-size:1.65rem; color:#fda4af;">₹{total_leakage:,}</div>
      <div style="font-size:0.75rem; color:#cbd5e1;">Fizul: <b>₹{fizul:,}</b> • Bad SL: <b>₹{bad_sl:,}</b></div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# DESIGN #9: 5-TAB NAVIGATION DOCK
# ------------------------------------------------------------------------------
tabs = st.tabs([
    "⚡ 0. Master Dock (#6 + #9 Fusion)",
    "🎯 1. Daily Trade & Rozmarra",
    "🔄 2. Bandhe Monthly Bills (Auto-Tag)",
    "📊 3. Interactive Bar Charts",
    "🧠 4. AI-CA & ITR-3 Tax Vault",
    "🏦 5. Bank + Broker Reconciler & 8 Indian Upgrades"
])

# TAB 0: MASTER COMMAND DOCK
with tabs[0]:
    st.markdown("""
    <div class="bento-card bento-violet" style="border: 2px solid rgba(6, 182, 212, 0.65);">
      <div style="font-size:0.75rem; font-weight:900; color:#6ee7b7; text-transform:uppercase;">
        🌅 SANDHYA 7–8 PM SMART AI DIARY • CHITRAGUPTA NLU AUTO-CLASSIFIER
      </div>
      <h4 style="margin:4px 0; color:#ffffff;">
        ✍️ Aaj Ka Pura Din, Trades & Kharch Likhein — AI Apne-Aap Saare 5 Tabs Update Karega
      </h4>
    </div>
    """, unsafe_allow_html=True)

    d_col1, d_col2, d_col3 = st.columns([1.2, 2.2, 1.2])
    with d_col1:
        diary_date = st.date_input("📅 Diary Date", value=date(2026, 11, 15), key="sandhya_date_inp")
    with d_col2:
        sample_choice = st.selectbox("⚡ Test Sample Evening Diary", list(DIARY_SAMPLES_PY.keys()), key="sandhya_sample_sel")
    with d_col3:
        dedup_bandhe = st.checkbox("Smart Bandhe-Bill De-Dup", value=True, key="sandhya_dedup_chk")

    diary_text = st.text_area(
        "Hinglish / Hindi / English Daily Diary (7–8 PM):",
        value=DIARY_SAMPLES_PY[sample_choice],
        height=95,
        key="sandhya_text_area"
    )

    parsed_preview = parse_sandhya_diary_text(diary_text, str(diary_date), st.session_state.recurring_bills, dedup_bandhe)

    pv1, pv2, pv3, pv4 = st.columns(4)
    with pv1:
        st.markdown(f"**🎯 Detected Trades ({len(parsed_preview['trades'])})**")
        for t in parsed_preview["trades"]:
            sign = "+" if t["pnl"] >= 0 else ""
            st.caption(f"• **{t['strike']}**: `{sign}₹{t['pnl']:,}` ({t['why']} | {t['sl_type']})")
    with pv2:
        st.markdown(f"**🛒 Classified Kharch ({len(parsed_preview['expenses'])})**")
        for e in parsed_preview["expenses"]:
            sync_tag = " 🔄 *(Bandha Sync)*" if e["matched_bandha_id"] else ""
            st.caption(f"• **{e['title']}**: `₹{e['amount']:,}` → `{e['category']}`{sync_tag}")
    with pv3:
        st.markdown(f"**📖 Dinacharya Notes ({len(parsed_preview['activities'])})**")
        for a in parsed_preview["activities"]:
            st.caption(f"• {a}")
    with pv4:
        pass_cnt = sum(parsed_preview["habit_updates"])
        st.markdown(f"**📅 Day D{diary_date.day} Habits ({pass_cnt}/6)**")
        h_labels = ["3-Lock", "No MidBox", "Smart SL", "Zero Greed", "Logged", "No Fizul"]
        badges = " | ".join(f"{'✅' if v == 1 else '❌'} {h_labels[i]}" for i, v in enumerate(parsed_preview["habit_updates"]))
        st.caption(badges)

    if st.button("🚀 AUTO-ADD DIARY TO ALL 5 TABS (TRADES + KHARCH + ITR-3 + HABITS)", use_container_width=True, type="primary"):
        for t in parsed_preview["trades"]:
            st.session_state.trades.append(t)
        new_exp_c = 0
        sync_b_c = 0
        for e in parsed_preview["expenses"]:
            if e["matched_bandha_id"]:
                for b in st.session_state.recurring_bills:
                    if b["id"] == e["matched_bandha_id"]:
                        b["amount"] = e["amount"]
                        b["active"] = True
                        sync_b_c += 1
            else:
                st.session_state.expenses.append({
                    "date": e["date"],
                    "title": e["title"],
                    "amount": e["amount"],
                    "category": e["category"]
                })
                new_exp_c += 1
        d_idx = max(0, min(30, diary_date.day - 1))
        for r_i, h_row in enumerate(st.session_state.habits):
            while len(h_row["days"]) <= d_idx:
                h_row["days"].append(1)
            h_row["days"][d_idx] = parsed_preview["habit_updates"][r_i]
        st.session_state.diary_logs.append({
            "date": str(diary_date),
            "raw_text": diary_text,
            "activities": parsed_preview["activities"],
            "summary_badge": f"{len(parsed_preview['trades'])} Trades • {new_exp_c} Kharch • {sync_b_c} Bandhe Synced"
        })
        st.rerun()

    c_left, c_mid, c_right = st.columns([1.05, 1.05, 1.1])
    with c_left:
        st.markdown("""
        <div class="bento-card bento-violet">
          <h4 style="margin:0 0 6px 0; color:#e9d5ff;">🔄 1st-OF-MONTH AUTO-TAGGED BILLS (DESIGN #6)</h4>
          <p style="font-size:0.78rem; color:#cbd5e1; margin-bottom:8px;">
            Toggle <b>ON</b> rakhein—AI-CA har mahine Wi-Fi, Mobile, Brokerage/STT, iPad Deprec. aur Ghar bills apne-aap jod lega:
          </p>
        </div>
        """, unsafe_allow_html=True)
        for idx, b in enumerate(st.session_state.recurring_bills):
            st.session_state.recurring_bills[idx]["active"] = st.toggle(
                f"{b['title']} — ₹{b['amount']:,} ({b['code']})",
                value=b["active"],
                key=f"dock_tog_{b['id']}"
            )

    with c_mid:
        ration_days = max(1, round(bad_sl / 450))
        st.markdown(f"""
        <div class="bento-card bento-emerald">
          <h4 style="margin:0 0 8px 0; color:#6ee7b7;">🧠 TRINETRA AI-CA LIVE BRAIN AUDITOR</h4>
          <div style="padding:10px; border-radius:12px; background:rgba(88,28,135,0.35); border:1px solid #8b5cf6; margin-bottom:8px; font-size:0.82rem;">
            <b>🟣 1. ITR-3 Section 37 & 32 Tax Shield:</b><br/>
            Auto-tagged <b>₹{total_sec37:,}/mo</b> (Wi-Fi, Mobile, TradingView, Brokerage/STT, iPad Deprec.) reduces your taxable F&O profit from <b>₹{net_pnl:,}</b> down to <b>₹{net_taxable_fo:,}</b>!
          </div>
          <div style="padding:10px; border-radius:12px; background:rgba(136,19,55,0.35); border:1px solid #f43f5e; margin-bottom:8px; font-size:0.82rem;">
            <b>🔴 2. Fizul Kharch + Bad SL Shock Audit:</b><br/>
            Is mahine <b>Bad SL (₹{bad_sl:,}) + Fizul Kharch (₹{fizul:,}) = ₹{total_leakage:,}</b> barbaad hua—jo aapke ghar ke <b>{ration_days} din ke Ration & Doodh</b> ke barabar hai!
          </div>
          <div style="padding:10px; border-radius:12px; background:rgba(8,51,68,0.45); border:1px solid #06b6d4; font-size:0.82rem;">
            <b>🔵 3. Section 44AB Digital Audit Check:</b><br/>
            Monthly ICAI Turnover: <b>₹{monthly_turnover:,}</b> (Well within the <b>₹10 Crore</b> Digital F&O Audit Limit).
          </div>
        </div>
        """, unsafe_allow_html=True)

    with c_right:
        st.markdown("""
        <div class="bento-card bento-cyan">
          <h4 style="margin:0 0 6px 0; color:#67e8f9;">📊 5-COLOR MONTHLY CASHFLOW & ITR-3 BAR CHART (₹)</h4>
        </div>
        """, unsafe_allow_html=True)
        chart_df = pd.DataFrame({
            "Bucket": ["1. Bandhe Ghar", "2. Rozmarra", "3. ITR-3 Auto", "4. 80C SIP/Save", "5. Tyohar Buf", "6. Fizul+Bad SL"],
            "Amount (₹)": [bandhe_ghar, rozmarra, total_sec37, sip_80c, tyohar, total_leakage]
        }).set_index("Bucket")
        st.bar_chart(chart_df, height=280)

# TAB 1: DAILY TRADE & ROZMARRA LOGGER
with tabs[1]:
    col_t, col_e = st.columns(2)
    with col_t:
        st.subheader("🎯 Log Today's Trade Psychology")
        t_strike = st.text_input("Strike / Instrument", "NIFTY 25150 CE")
        t_pnl = st.number_input("Net P&L (₹) (+Win / -Loss)", value=4500, step=500)
        t_why = st.selectbox("1. Maine Aaj Trade Kyo Liya?", [
            "3-Lock + 7-EMA Root",
            "Wyckoff Spring Reclaim",
            "Running Candle FOMO",
            "Sideways Mid-Box Guess",
            "Revenge Trade"
        ])
        t_sl = st.selectbox("2. Outcome / SL Audit", [
            "Target Hit (T1/T2/T3)",
            "Good System SL",
            "Bad Mistake SL"
        ])
        t_greed = st.selectbox("3. Profit Greed Check", [
            "Disciplined Trail (Zero Greed)",
            "Target Greed (Didn't Trail)",
            "Quota Greed (Overtraded)"
        ])
        t_note = st.text_input("1-Line Lesson", "Waited for 3-Lock + 7-EMA root pullback.")
        if st.button("🏹 Save Trade Entry", use_container_width=True):
            st.session_state.trades.append({
                "date": str(date.today()),
                "strike": t_strike,
                "pnl": t_pnl,
                "why": t_why,
                "sl_type": t_sl,
                "greed": t_greed,
                "note": t_note
            })
            st.rerun()
        st.dataframe(pd.DataFrame(st.session_state.trades), use_container_width=True)

    with col_e:
        st.subheader("🛒 Log Daily Rozmarra / Fizul Kharch")
        e_title = st.text_input("Kharch Ka Naam (e.g. Sabzi, Petrol, Zomato)", "Taaza Sabzi & Phal")
        e_amt = st.number_input("Amount (₹)", value=200, step=50)
        e_cat = st.selectbox("5-Color Indian Cashflow Bucket", [
            "Rozmarra Essential",
            "ITR-3 Business Deduct",
            "SIP & 80C/80D Wealth",
            "Tyohar & Emergency",
            "Fizul Kharch"
        ])
        if st.button("💳 Save Expense Entry", use_container_width=True):
            st.session_state.expenses.append({
                "date": str(date.today()),
                "title": e_title,
                "amount": e_amt,
                "category": e_cat
            })
            st.rerun()
        st.dataframe(pd.DataFrame(st.session_state.expenses), use_container_width=True)

# TAB 2: BANDHE MONTHLY BILLS
with tabs[2]:
    st.subheader("🔄 Edit 1st-of-Month Auto-Tagged Recurring Bills")
    for idx, b in enumerate(st.session_state.recurring_bills):
        c1, c2, c3 = st.columns([2.5, 1, 1])
        with c1:
            st.write(f"**{b['title']}** (`{b['category']} • {b['code']}`)")
        with c2:
            st.session_state.recurring_bills[idx]["amount"] = st.number_input(
                "₹/mo", value=int(b["amount"]), step=100, key=f"amt_{b['id']}", label_visibility="collapsed"
            )
        with c3:
            st.session_state.recurring_bills[idx]["active"] = st.checkbox(
                "Auto-Tag ON", value=b["active"], key=f"chk_{b['id']}"
            )

# TAB 3: INTERACTIVE BAR CHARTS
with tabs[3]:
    ch1, ch2 = st.columns(2)
    with ch1:
        st.subheader("📊 5-Color Monthly Cashflow Breakdown (₹)")
        st.bar_chart(chart_df, height=340)
    with ch2:
        st.subheader("📈 Trading Psychology: Sniper Wins vs Good/Bad SL (₹)")
        psych_df = pd.DataFrame({
            "Category": ["1. 3-Lock Gross Win", "2. Good System SL", "3. Bad Mistake SL", "4. Fizul Kharch", "5. Net Trading P&L"],
            "Amount (₹)": [gross_win, good_sl, bad_sl, fizul, net_pnl]
        }).set_index("Category")
        st.bar_chart(psych_df, height=340)

# TAB 4: AI-CA & ITR-3 VAULT
with tabs[4]:
    st.subheader("📄 CA-Ready ITR-3 Schedule BP (Business & Profession) Summary")
    itr_df = pd.DataFrame([
        {"ITR-3 Schedule BP Line Item": "1. Gross F&O Business Profit (Sec 43(5) • Code 13018)", "Amount (₹)": net_pnl},
        {"ITR-3 Schedule BP Line Item": "2. Less: Auto-Tagged Sec 37 & 32 Business Deductions (Wi-Fi, Mobile, Brokerage/STT, iPad Deprec.)", "Amount (₹)": -total_sec37},
        {"ITR-3 Schedule BP Line Item": "3. Net Taxable F&O Business Income", "Amount (₹)": net_taxable_fo},
        {"ITR-3 Schedule BP Line Item": "4. Chapter VI-A Deductions Tracked (Sec 80C SIP + Sec 80D Mediclaim)", "Amount (₹)": sip_80c},
        {"ITR-3 Schedule BP Line Item": "5. ICAI Section 44AB Monthly Turnover (Digital Limit ₹10 Crore)", "Amount (₹)": monthly_turnover},
    ])
    st.table(itr_df)
    csv_bytes = itr_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download CA-Ready ITR-3 Schedule BP CSV",
        data=csv_bytes,
        file_name="RAGHAVA_ASTRA_TRINETRA_ITR3_SUMMARY.csv",
        mime="text/csv"
    )

# TAB 5: MONTHLY BANK STATEMENT + BROKER P&L RECONCILER & 8 INDIAN UPGRADES
with tabs[5]:
    st.subheader("🏦 Monthly Bank Statement + Broker Tax P&L Auto-Reconciler")
    up_c1, up_c2, up_c3 = st.columns([1.4, 1.4, 1.2])
    with up_c1:
        broker_csv = st.file_uploader("📈 1. Upload Broker P&L CSV (Angel One / Zerodha / Dhan)", type=["csv", "txt"], key="py_brok_csv")
        if broker_csv is not None:
            df_b = pd.read_csv(broker_csv)
            num_cols = df_b.select_dtypes(include="number").columns
            if len(num_cols) > 0:
                gross_val = int(df_b[num_cols[-1]].sum())
                chg_val = int(len(df_b) * 65 + abs(gross_val) * 0.06)
                st.session_state.reconcile_data["broker_gross_pnl"] = gross_val
                st.session_state.reconcile_data["broker_charges"] = chg_val
                st.session_state.reconcile_data["broker_net_pnl"] = gross_val - chg_val
                st.session_state.reconcile_data["broker_trade_count"] = len(df_b)
    with up_c2:
        bank_csv = st.file_uploader("🏦 2. Upload Monthly Bank Statement CSV (SBI / HDFC / ICICI)", type=["csv", "txt"], key="py_bank_csv")
        if bank_csv is not None:
            df_k = pd.read_csv(bank_csv)
            num_cols = df_k.select_dtypes(include="number").columns
            if len(num_cols) > 0:
                s_vals = df_k[num_cols[0]].dropna()
                st.session_state.reconcile_data["bank_total_upi_debits"] = int(s_vals[s_vals > 0].sum())
                chillar_s = s_vals[(s_vals >= 10) & (s_vals <= 100)]
                st.session_state.reconcile_data["bank_chillar_count"] = int(len(chillar_s))
                st.session_state.reconcile_data["bank_chillar_amount"] = int(chillar_s.sum())
    with up_c3:
        st.session_state.base_capital = st.number_input("🛡️ Base Trading Capital (₹)", value=int(st.session_state.base_capital), step=10000)
        roi_pct = round((net_pnl / max(10000, st.session_state.base_capital)) * 100, 1)
        max_daily_sl = round(st.session_state.base_capital * 0.02)
        st.caption(f"**Live Monthly ROI:** `{roi_pct}%` • **Max 2% Daily SL:** `₹{max_daily_sl:,}`")
        if st.button("🔄 Sync Broker Charges & Chillar UPI to Journal", use_container_width=True):
            for b in st.session_state.recurring_bills:
                if b["id"] == "b4":
                    b["amount"] = st.session_state.reconcile_data["broker_charges"]
                    b["active"] = True
            if st.session_state.reconcile_data["bank_chillar_amount"] > 0:
                st.session_state.expenses.append({
                    "date": str(date.today()),
                    "title": f"Bank Statement Chillar UPI ({st.session_state.reconcile_data['bank_chillar_count']} scans <₹100)",
                    "amount": st.session_state.reconcile_data["bank_chillar_amount"],
                    "category": "Fizul Kharch"
                })
                st.session_state.reconcile_data["bank_chillar_amount"] = 0
            st.rerun()

    rc = st.session_state.reconcile_data
    logged_tot = total_grihasthi + tyohar + fizul
    upi_gap = max(0, rc["bank_total_upi_debits"] - logged_tot)
    rc1, rc2, rc3, rc4 = st.columns(4)
    rc1.metric("1. Broker Gross vs Charges", f"₹{rc['broker_gross_pnl']:,}", f"-₹{rc['broker_charges']:,} STT/Brok/GST")
    rc2.metric("2. Unlogged Bank UPI Gap", f"₹{upi_gap:,}", f"{rc['bank_chillar_count']} Chillar UPI (₹{rc['bank_chillar_amount']:,})")
    rc3.metric("3. Friday Bank Payout Locked", f"₹{st.session_state.bank_payout_locked:,}", f"{round(st.session_state.bank_payout_locked / max(1, net_pnl) * 100)}% Withdrawn")
    rc4.metric("4. Advance Tax Gullak (15%)", f"₹{round(net_taxable_fo * 0.15):,}", f"🧘‍♂️ {st.session_state.patience_days} Patience Days")

    st.markdown("---")
    u_col1, u_col2 = st.columns(2)
    with u_col1:
        st.subheader("🤝 1. Dosto Ki Udhaari & Split-Bill Vasooli Tracker")
        u_person = st.text_input("Dost Ka Naam & Reason", "Rahul (Dinner Split)")
        u_amt = st.number_input("Amount (₹)", value=600, step=100, key="py_u_amt")
        if st.button("➕ Add Udhaari Record", use_container_width=True):
            st.session_state.udhaari_list.append({
                "id": f"u_{len(st.session_state.udhaari_list)+1}",
                "person": u_person,
                "amount": u_amt,
                "type": "Vasoolna Hai (Lent)",
                "settled": False,
                "date": str(date.today())
            })
            st.rerun()
        st.dataframe(pd.DataFrame(st.session_state.udhaari_list), use_container_width=True)

    with u_col2:
        st.subheader("🏧 2. Friday Bank Payout Lock & 0-Trade Sniper Patience")
        pay_add = st.number_input("Lock Profit to Safe Bank Account (₹)", value=10000, step=1000)
        if st.button("🏦 +Lock Profit to Bank Account", use_container_width=True):
            st.session_state.bank_payout_locked += pay_add
            st.rerun()
        if st.button("🧘‍♂️ +Log Zero-Trade Sniper Patience Day (Capital Saved!)", use_container_width=True):
            st.session_state.patience_days += 1
            st.rerun()