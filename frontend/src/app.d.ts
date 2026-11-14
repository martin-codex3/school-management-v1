// See https://svelte.dev/docs/kit/types#app.d.ts

import type { Token } from "#lib/types/token/token.ts";
import type { UserResponse } from "#lib/types/users/user_response.ts";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			token: string | undefined,
			user: UserResponse | null
		}
		interface PageData { }
		// interface PageState {}
		// interface Platform {}
	}
}

export { };
