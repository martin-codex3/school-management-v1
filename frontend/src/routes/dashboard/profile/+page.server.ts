import { fail, redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";
import { requiresLogin } from "#lib/server/auth.ts";
import { PUBLIC_BACKEND_API } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/errors/validation_errors.ts";

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/");
    }

    return { user }
}

export const actions: Actions = {
    updateProfile: async ({ request, fetch, locals }) => {
        const user = locals.user;
        const token = locals.token;

        if (!user) {
            redirect(307, "/");
        }

        const data = await request.formData();
        const payload = Object.fromEntries(data);

        const response = await fetch(`${PUBLIC_BACKEND_API}/users/update-account/${user.id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const responseData: ValidationErrors = await response.json();
            return fail(response.status, { problem: responseData });
        }

        return { success: true }
    },

    // for logging the users out 
    logOutUsers: async ({ cookies }) => {
        cookies.delete("access_token", { path: "/" })
    }
}