import { Link } from "react-router-dom";
import { BrainCircuit } from "lucide-react";

export default function Register() {
  return (
    <div className="auth-page">
      <div className="auth-container">

        <section className="auth-info">
          <div className="auth-brand">
            <div className="auth-brand-icon">
              <BrainCircuit size={25} />
            </div>

            <div className="auth-brand-text">
              <div className="auth-brand-name">
                MEDXAI
              </div>

              <div className="auth-brand-subtitle">
                Spatial Intelligence
              </div>
            </div>
          </div>

          <h1>
            Start your
            <span>AI journey.</span>
          </h1>

          <p className="auth-description">
            Create your MedXAI workspace and explore
            explainable MRI analysis powered by artificial
            intelligence.
          </p>
        </section>

        <section className="auth-card">

          <div className="auth-header">
            <h2>Create account</h2>

            <p>
              Set up your MedXAI researcher account.
            </p>
          </div>

          <form className="auth-form">

            <div className="auth-field">
              <label>Full name</label>

              <input
                type="text"
                placeholder="Your name"
                required
              />
            </div>

            <div className="auth-field">
              <label>Email address</label>

              <input
                type="email"
                placeholder="researcher@example.com"
                required
              />
            </div>

            <div className="auth-field">
              <label>Password</label>

              <input
                type="password"
                placeholder="Create a password"
                required
              />
            </div>

            <button
              type="submit"
              className="auth-submit"
            >
              Create account
            </button>

          </form>

          <div className="auth-switch">
            Already have an account?

            <Link to="/login">
              Sign in
            </Link>
          </div>

        </section>

      </div>
    </div>
  );
}