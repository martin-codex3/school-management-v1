import type { Actions } from "./$types";
import { PUBLIC_BACKEND_API } from '$app/env/public';

export const actions: Actions = {
    createAccount: async ({ fetch, request }) => {
        const data = await request.formData();

        const first_name = data.get("first_name")?.toString().trim() ?? "";
        const last_name = data.get("last_name")?.toString().trim() ?? "";
        const email = data.get("email")?.toString().trim() ?? "";
        const phone_number = data.get("phone_number")?.toString().trim() ?? "";
        const password_hash = data.get("password_hash")?.toString().trim() ?? ""
        const school_name = data.get("school_name")?.toString().trim() ?? "";
        const school_type = data.get("school_type")?.toString().trim() ?? "";
        const school_email = data.get("school_email")?.toString().trim() ?? "";
        const school_phone = data.get("school_phone")?.toString().trim() ?? "";
        const address = data.get("address")?.toString().trim() ?? "";
        const city = data.get("city")?.toString().trim() ?? "";
        const country = data.get("country")?.toString().trim() ?? "";

        const payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "school_name": school_name,
            "school_type": school_type,
            "school_email": school_email,
            "school_phone": school_phone,
            "address": address,
            "city": city,
            "country": country,
            "password_hash": password_hash
        }

        const response = await fetch(`${PUBLIC_BACKEND_API}/authentication/create-account`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            console.log(await response.json())
        }

        return { success: true }

    }
}