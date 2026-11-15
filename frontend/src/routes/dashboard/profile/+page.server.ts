import { redirect, type Actions } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";
import { requiresLogin } from "#lib/server/auth.ts";

export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/");
    }

    return { user }
}

export const actions: Actions = {
    updateProfile: async ({ request }) => {
        requiresLogin;

        const data = await request.formData();

        console.log(data)
    }
}