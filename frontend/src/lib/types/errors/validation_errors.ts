export interface ErrorDetails {
    code: string,
    detail: string,
    pointer: string
}

export interface ValidationErrors {
    type: string,
    title: string,
    status: number,
    code: string,
    errors: ErrorDetails[]
}