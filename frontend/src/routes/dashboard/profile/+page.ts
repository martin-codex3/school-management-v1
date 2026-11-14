import { requiresLogin } from "#lib/server/auth.ts";
import { redirect } from "@sveltejs/kit";
import type { PageLoad } from "./$types";

export const load: PageLoad = ({ locals }) => {
    const user = locals.user;

    if (!user) {
        redirect(307, "/");
    }

    return { user: user }
}