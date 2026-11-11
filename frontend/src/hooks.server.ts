import { resolve } from "$app/paths";
import type { Handle } from "@sveltejs/kit/hooks";

export const handle: Handle = async ({ event, resolve }) => {

    const response = await resolve(event);
    return response
}