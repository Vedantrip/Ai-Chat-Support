# Threadlane business setup (fictional demo)

Threadlane is a placeholder clothing brand created for this local prototype. It is not Bonkers and is not connected to any real business.

## Current action

`lookup_order` is a read-only demo action. It requires both the order number and the email associated with the order. The backend checks both values before returning status and item information. It never changes an order and never returns the stored email address.

## Data and policy limits

- `data/demo_orders.json` contains fabricated records using reserved `.test` email addresses. Do not replace these with real customer data until access controls and a real store integration are designed.
- No real store, order system, shipping carrier, return policy, or refund policy is connected or defined.
- The assistant must identify lookup results as demo data and must not invent business policies.
- Add real FAQs and policies to `knowledge/faq.md` only after confirming the business's actual rules.