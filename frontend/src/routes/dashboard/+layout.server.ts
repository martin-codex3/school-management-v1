import { requiresLogin } from "#lib/server/auth.ts";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    const user = requiresLogin;

    return user
}