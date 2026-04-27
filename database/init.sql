CREATE TABLE IF NOT EXISTS visit_invoices (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

