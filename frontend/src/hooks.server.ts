import { resolve } from "$app/paths";
import { error, fail, redirect } from "@sveltejs/kit";
import type { Handle } from "@sveltejs/kit/hooks";
import { PUBLIC_BACKEND_API } from "$app/env/public"
import type { ValidationErrors } from "#lib/types/errors/validation_errors.ts";
import type { UserResponse } from "#lib/types/users/user_response.ts";

export const handle: Handle = async ({ event, resolve }) => {

    event.locals.token = event.cookies.get("access_token");
    const access_token = event.locals.token;
    event.locals.user = null;

    if (!access_token) {
        if (event.url.pathname.startsWith("/dashboard")) {
            redirect(307, "/")
        }
    }

    if (access_token) {
        const response = await fetch(`${PUBLIC_BACKEND_API}/authentication/me`, {
            method: "GET",
            headers: { "Content-Type": "application/json", "Authorization": `Bearer ${access_token}` }
        });

        if (response.status === 401 || response.status === 403) {
            event.cookies.delete("access_token", { path: "/" });
        } else if (!response.ok) {
            error(response.status, "Something went wrong!")
        } else {
            const responseData: UserResponse = await response.json();
            event.locals.user = responseData
        }
    }

    const response = await resolve(event);
    return response
}