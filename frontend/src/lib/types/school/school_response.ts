export interface ApplicationUsers {
    application_user_id: string,
    tenant_id: string,
    updated_date: string,
    id: string,
    created_date: string
}

export interface SchoolResponse {
    id: string;
    school_name: string
    school_type: string
    school_email: string
    school_phone: string
    address: string
    city: string
    country: string
    website_url: string | undefined
    registration_number: string | undefined
    school_code: string | undefined
    description: string | undefined
    settings: object
    display_name: string | undefined
    secondary_email: string | undefined
    ownership_type: string | undefined
    official_contact_person: string | undefined
    contact_person_email: string | undefined
    contact_person_phone: string | undefined
    district: string | undefined
    region: string | undefined
    postal_code: string | undefined
    application_users: ApplicationUsers[]
}