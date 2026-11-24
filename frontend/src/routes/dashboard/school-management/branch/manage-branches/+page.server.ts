import { error, redirect } from "@sveltejs/kit";
import type { Actions, PageServerLoad } from "./$types";
import { PUBLIC_BACKEND_API } from "$app/env/public";

export const load: PageServerLoad = async ({ locals, fetch }) => {
    const current_user = locals.user;

    if (!current_user) {
        redirect(307, "/");
    }

    const access_token = locals.token;

    // we will attempt to fetch the branches here 
    const response = await fetch(`${PUBLIC_BACKEND_API}/branches/${current_user.id}/tenant-branches`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    });

    if (!response.ok) {
        error(response.status, "Failed to fetch the branches");
    }

    const branches = await response.json();

    return { branches }
}