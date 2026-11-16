import { error, redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "./$types";
import { PUBLIC_BACKEND_API } from "$app/env/public";
import type { SchoolResponse } from "#lib/types/school/school_response.ts";


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

        error(response.status, "Failed to fetch the record");
    }

    const school: SchoolResponse = await response.json();
    return { school }

}