// See https://svelte.dev/docs/kit/types#app.d.ts

import type { Token } from "#lib/types/token/token.ts";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			token: string | undefined,
			user: {}
		}
		interface PageData { }
		// interface PageState {}
		// interface Platform {}
	}
}

export { };
