import { getRequestEvent } from "$app/server"
import { redirect } from "@sveltejs/kit";

export const requiresLogin = () => {
    const { locals, url } = getRequestEvent();

    if (!locals.user) {
        redirect(303, "/")
    }


    return locals.user
}