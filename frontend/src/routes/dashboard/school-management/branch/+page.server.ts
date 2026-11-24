import { fail, redirect, type Actions } from "@sveltejs/kit";
import { PUBLIC_BACKEND_API } from "$app/env/public";
import type { ValidationErrors } from "#lib/types/errors/validation_errors.ts";

export const actions: Actions = {
    createBranch: async ({ request, fetch, locals }) => {
        const user = locals.user;

        if (!user) {
            redirect(307, "/")
        }

        const access_token = locals.token;

        const data = await request.formData();

        const branch_name = data.get("branch_name");
        const branch_email = data.get("branch_email");
        const branch_phone = data.get("branch_phone");
        const alternative_phone = data.get("alternative_phone");
        const address_line_1 = data.get("address_line_1");
        const address_line_2 = data.get("address_line_2");
        const city = data.get("city");
        const nationality = data.get("nationality");
        const district = data.get("district");
        const is_main_branch = data.get("is_main_branch");


        const payload = {
            "branch_name": branch_name,
            "branch_email": branch_email,
            "branch_phone": branch_phone,
            "alternative_phone": alternative_phone,
            "address_line_1": address_line_1,
            "address_line_2": address_line_2,
            "city": city,
            "nationality": nationality,
            "district": district,
            "is_imain_branch": is_main_branch
        }


        // we will create the branch here
        const response = await fetch(`${PUBLIC_BACKEND_API}/branches/${user.id}`, {
            method: "POST",
            headers: { "Content-Type": "application/json", "Authorization": `Bearer ${access_token}` },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            return fail(response.status, { problem: responseData });
        }

        return { success: true }
    }
}