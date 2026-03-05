import { Resend } from "resend";
import { NextResponse } from "next/server";

const resend = new Resend(process.env.RESEND_API_KEY);
const ZAPIER_WEBHOOK = "https://hooks.zapier.com/hooks/catch/26639307/u0709gu/";

export async function POST(req: Request) {
  const { firstName, lastName, email, business, service, message } = await req.json();

  // Send email via Resend
  const { error } = await resend.emails.send({
    from: "Apex Growth Contact <noreply@apexgrowthmanagement.com>",
    to: "admin@apexgrowthmanagement.com",
    subject: `New inquiry from ${firstName} ${lastName}`,
    html: `
      <h2>New Contact Form Submission</h2>
      <p><strong>Name:</strong> ${firstName} ${lastName}</p>
      <p><strong>Email:</strong> ${email}</p>
      <p><strong>Business:</strong> ${business || "Not provided"}</p>
      <p><strong>Service:</strong> ${service || "Not selected"}</p>
      <p><strong>Message:</strong></p>
      <p>${message}</p>
    `,
  });

  if (error) {
    return NextResponse.json({ error }, { status: 500 });
  }

  // Send to Zapier webhook
  await fetch(ZAPIER_WEBHOOK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ firstName, lastName, email, business, service, message }),
  });

  return NextResponse.json({ success: true });
}
