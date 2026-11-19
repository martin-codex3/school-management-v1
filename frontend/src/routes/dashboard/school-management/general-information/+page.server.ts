import { fail, redirect, type Actions } from "@sveltejs/kit";
import { PUBLIC_BACKEND_API } from "$app/env/public";
import type { ValidationErrors } from "#lib/types/errors/validation_errors.ts";

export const actions: Actions = {
    updateSchoolDetails: async ({ request, locals }) => {

        const user = locals.user;

        if (!user) {
            redirect(307, "/");
        }

        // we will update the users here 
        const access_token = locals.token;
        const data = await request.formData();
        const payload = Object.fromEntries(data);


        const response = await fetch(`${PUBLIC_BACKEND_API}/tenants`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            return fail(response.status, { problem: responseData });
        }

        console.log(payload);


        return { success: true }
    }
}