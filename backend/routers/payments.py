from fastapi import APIRouter
import stripe, requests, os

router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
PAYSTACK_KEY = os.getenv("PAYSTACK_SECRET_KEY")

@router.post("/stripe")
def stripe_checkout(email: str, price_id: str):
    session = stripe.checkout.Session.create(
        customer_email=email,
        mode="subscription",
        line_items=[{"price": price_id, "quantity": 1}],
        success_url="https://proscore.ai/success",
        cancel_url="https://proscore.ai/cancel"
    )
    return {"url": session.url}

@router.post("/paystack")
def paystack_checkout(email: str, amount: float):
    return requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers={"Authorization": f"Bearer {PAYSTACK_KEY}"},
        json={"email": email, "amount": int(amount*100)}
    ).json()
