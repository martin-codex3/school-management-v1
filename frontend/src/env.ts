import { defineEnvVars } from "@sveltejs/kit/env";

export const variables = defineEnvVars({
    PUBLIC_BACKEND_API: { public: true }
});