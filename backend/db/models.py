from sqlalchemy import Boolean, Column, Integer, String, Text, Date, DateTime, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


# ============================================================================
# TABLE 1: USER_CLIENTS (Client Accounts)
# ============================================================================
class UserClient(Base):
    __tablename__ = "user_clients"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String(10))
    last_login = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    client = relationship("Client", back_populates="user", uselist=False)


# ============================================================================
# TABLE 2: POSITIONS (Employee Positions)
# ============================================================================
class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text)
    access_level = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    employees = relationship("Employee", back_populates="position")


# ============================================================================
# TABLE 3: EMPLOYEES (Employees)
# ============================================================================
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    position_id = Column(Integer, ForeignKey("positions.id", ondelete="RESTRICT"), nullable=False, index=True)
    phone = Column(String(20))
    email = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=True, index=True)
    hire_date = Column(Date)
    last_login = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    position = relationship("Position", back_populates="employees")
    verifications = relationship("TenantVerification", back_populates="verified_by_employee")
    contracts = relationship("Contract", back_populates="employee")


# ============================================================================
# TABLE 4: COMPANIES (Partner Companies)
# ============================================================================
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    inn = Column(String(12), unique=True, index=True)
    legal_address = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    clients = relationship("Client", back_populates="company")


# ============================================================================
# TABLE 5: CLIENTS (Client Profiles)
# ============================================================================
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_clients.id", ondelete="SET NULL"), unique=True, index=True)
    full_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date)
    passport_series = Column(String(10))
    passport_number = Column(String(20))
    passport_issued_by = Column(Text)
    passport_issue_date = Column(Date)
    phone = Column(String(20), nullable=False, index=True)
    email = Column(String(255), index=True)
    alternative_phone = Column(String(20))
    registration_address = Column(Text)
    actual_address = Column(Text)
    workplace = Column(String(255))
    position = Column(String(255))
    monthly_income = Column(Numeric(10, 2))
    is_verified = Column(Boolean, default=False, index=True)
    client_type = Column(String(20), default='individual')
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="SET NULL"))
    registration_date = Column(Date, server_default=func.current_date())
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("client_type IN ('individual', 'legal_entity')", name='check_client_type'),
    )

    # Relationships
    user = relationship("UserClient", back_populates="client")
    company = relationship("Company", back_populates="clients")
    applications = relationship("Application", back_populates="client")
    verifications = relationship("TenantVerification", back_populates="client")
    contracts = relationship("Contract", back_populates="client")
    reviews = relationship("Review", back_populates="client")


# ============================================================================
# TABLE 6: PROPERTIES (Real Estate Properties)
# ============================================================================
class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(20), nullable=False, index=True)
    subtype = Column(String(100))
    address = Column(Text, nullable=False)
    area = Column(Numeric(10, 2), nullable=False, index=True)
    rooms_count = Column(Integer)
    floor = Column(Integer)
    total_floors = Column(Integer)
    renovation_type = Column(String(100))
    is_furnished = Column(Boolean, default=False)
    monthly_rent = Column(Numeric(10, 2), nullable=False, index=True)
    utilities_included = Column(Boolean, default=False)
    deposit_amount = Column(Numeric(10, 2))
    description = Column(Text)
    amenities = Column(Text)
    photos = Column(Text)
    video_url = Column(String(500))
    status = Column(String(20), default='available', index=True)
    published_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("type IN ('commercial', 'residential')", name='check_property_type'),
        CheckConstraint("status IN ('available', 'reserved', 'rented', 'maintenance')", name='check_property_status'),
    )

    # Relationships
    applications = relationship("Application", back_populates="property")
    contracts = relationship("Contract", back_populates="property")
    reviews = relationship("Review", back_populates="property")


# ============================================================================
# TABLE 7: APPLICATIONS (Rental Applications)
# ============================================================================
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"), nullable=False, index=True)
    application_date = Column(Date, server_default=func.current_date(), index=True)
    status = Column(String(20), default='pending', index=True)
    preferred_move_in_date = Column(Date)
    lease_duration_months = Column(Integer)
    notes = Column(Text)
    rejection_reason = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('pending', 'under_review', 'approved', 'rejected', 'cancelled')", name='check_application_status'),
    )

    # Relationships
    client = relationship("Client", back_populates="applications")
    property = relationship("Property", back_populates="applications")


# ============================================================================
# TABLE 8: TENANT_VERIFICATIONS (Tenant Verifications)
# ============================================================================
class TenantVerification(Base):
    __tablename__ = "tenant_verifications"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, index=True)
    verified_by = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), index=True)
    verification_date = Column(Date, server_default=func.current_date(), index=True)
    income_verified = Column(Boolean, default=False)
    credit_score = Column(Integer)
    employment_verified = Column(Boolean, default=False)
    criminal_record_check = Column(Boolean, default=False)
    previous_rentals_check = Column(Boolean, default=False)
    result = Column(String(30), nullable=False, index=True)
    rejection_reason = Column(Text)
    notes = Column(Text)
    documents_checked = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("result IN ('approved', 'conditionally_approved', 'rejected')", name='check_verification_result'),
    )

    # Relationships
    client = relationship("Client", back_populates="verifications")
    verified_by_employee = relationship("Employee", back_populates="verifications")


# ============================================================================
# TABLE 9: CONTRACTS (Rental Contracts)
# ============================================================================
class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    contract_number = Column(String(50), unique=True, nullable=False, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"))
    signing_date = Column(Date, nullable=False)
    start_date = Column(Date, nullable=False, index=True)
    end_date = Column(Date, nullable=False, index=True)
    monthly_rent = Column(Numeric(10, 2), nullable=False)
    deposit_amount = Column(Numeric(10, 2))
    deposit_paid = Column(Boolean, default=False)
    contract_status = Column(String(20), default='active', index=True)
    payment_day = Column(Integer, default=1)
    payment_method = Column(String(50))
    additional_services = Column(Text)
    contract_file_url = Column(String(500))
    signed_electronically = Column(Boolean, default=False)
    termination_date = Column(Date)
    termination_reason = Column(Text)
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("contract_status IN ('active', 'expired', 'terminated', 'suspended')", name='check_contract_status'),
    )

    # Relationships
    client = relationship("Client", back_populates="contracts")
    property = relationship("Property", back_populates="contracts")
    employee = relationship("Employee", back_populates="contracts")
    payments = relationship("Payment", back_populates="contract")


# ============================================================================
# TABLE 10: PAYMENTS (Payments)
# ============================================================================
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    payment_date = Column(Date, nullable=False, index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    payment_type = Column(String(20), default='rent')
    payment_method = Column(String(50))
    payment_status = Column(String(20), default='pending', index=True)
    transaction_id = Column(String(100))
    period_month = Column(Integer, index=True)
    period_year = Column(Integer, index=True)
    is_late = Column(Boolean, default=False)
    late_days = Column(Integer, default=0)
    penalty_amount = Column(Numeric(10, 2), default=0)
    notes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("payment_type IN ('rent', 'deposit', 'utilities', 'service', 'penalty')", name='check_payment_type'),
        CheckConstraint("payment_status IN ('pending', 'completed', 'failed', 'refunded')", name='check_payment_status'),
    )

    # Relationships
    contract = relationship("Contract", back_populates="payments")


# ============================================================================
# TABLE 11: ADDITIONAL_SERVICES (Additional Services)
# ============================================================================
class AdditionalService(Base):
    __tablename__ = "additional_services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    unit = Column(String(50))
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


# ============================================================================
# TABLE 12: REVIEWS (Client Reviews)
# ============================================================================
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="SET NULL"), index=True)
    rating = Column(Integer, nullable=False)
    text = Column(Text)
    review_date = Column(Date, server_default=func.current_date())
    is_approved = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name='check_rating'),
    )

    # Relationships
    client = relationship("Client", back_populates="reviews")
    property = relationship("Property", back_populates="reviews")
