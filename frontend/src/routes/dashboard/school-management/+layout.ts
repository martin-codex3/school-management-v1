import { fail, redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "../$types";
import { PUBLIC_BACKEND_API } from "$app/env/public";
import type { ValidationErrors } from "#lib/types/errors/validation_errors.ts";

export const load: LayoutServerLoad = async ({ locals, fetch }) => {
    const user = locals.user;
    if (!user) {
        redirect(307, "/");
    }

    const access_token = locals.token;

    // we will fetch the tenant here
    const response = await fetch(`${PUBLIC_BACKEND_API}/tenants`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    });

    if (!response.ok) {
        const responseData: ValidationErrors = await response.json();
        return fail(response.status, { problem: responseData });
    }

    return { success: true }

}