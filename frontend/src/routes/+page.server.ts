import type { Actions } from "./$types";
import PUBLIC_BACKEND_API from '$app/env/public'

export const actions: Actions = {
    createAccount: async ({ fetch, request }) => {
        const data = await request.formData()

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


    }
}