import { redirect, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
    createBranch: async ({ request, fetch, locals }) => {
        const user = locals.user;

        if (!user) {
            redirect(307, "/")
        }

        const access_token = locals.token;

        // we will create the branch here
        console.log("hey mate");
    }
}