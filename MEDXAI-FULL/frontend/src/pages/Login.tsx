import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { BrainCircuit, ShieldCheck, Eye, EyeOff } from "lucide-react";
import { useAuth } from "../context/AuthContext";

export default function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");
    setLoading(true);

    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err: any) {
      setError(
        err?.message || "Unable to sign in. Please check your credentials."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-container">

        {/* LEFT PANEL */}

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
            Intelligence
            <span>for every scan.</span>
          </h1>

          <p className="auth-description">
            An explainable AI workspace for MRI analysis,
            designed to transform complex medical imaging
            into interpretable signals.
          </p>

          <div className="auth-features">

            <div className="auth-feature">
              <div className="auth-feature-icon">
                <BrainCircuit size={17} />
              </div>

              <div className="auth-feature-text">
                EfficientNetB0-powered MRI classification
              </div>
            </div>

            <div className="auth-feature">
              <div className="auth-feature-icon">
                <ShieldCheck size={17} />
              </div>

              <div className="auth-feature-text">
                Explainable Grad-CAM and LIME analysis
              </div>
            </div>

          </div>

        </section>

        {/* LOGIN CARD */}

        <section className="auth-card">

          <div className="auth-header">
            <h2>
              Welcome back.
            </h2>

            <p>
              Sign in to access your MedXAI workspace.
            </p>
          </div>

          <form
            className="auth-form"
            onSubmit={handleSubmit}
          >

            {error && (
              <div className="auth-error">
                {error}
              </div>
            )}

            <div className="auth-field">

              <label htmlFor="email">
                Email address
              </label>

              <input
                id="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="researcher@example.com"
                required
              />

            </div>

            <div className="auth-field">

              <label htmlFor="password">
                Password
              </label>

              <div className="auth-password-wrapper">

                <input
                  id="password"
                  type={showPassword ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter your password"
                  required
                />

                <button
                  type="button"
                  className="auth-password-toggle"
                  onClick={() =>
                    setShowPassword(!showPassword)
                  }
                >
                  {showPassword ? (
                    <EyeOff size={17} />
                  ) : (
                    <Eye size={17} />
                  )}
                </button>

              </div>

            </div>

            <div className="auth-options">

              <label className="auth-remember">
                <input type="checkbox" />
                Remember me
              </label>

              <button
                type="button"
                className="auth-forgot"
              >
                Forgot password?
              </button>

            </div>

            <button
              type="submit"
              className="auth-submit"
              disabled={loading}
            >
              {loading ? "Signing in..." : "Sign in"}
            </button>

          </form>

          <div className="auth-switch">
            Don't have an account?
            <Link to="/register">
              Create account
            </Link>
          </div>

          <div className="auth-security">
            <ShieldCheck size={13} />
            Secure authentication
          </div>

        </section>

      </div>
    </div>
  );
}