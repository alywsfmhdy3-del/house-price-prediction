import { useEffect, useState } from "react";
import {
  FACING_OPTIONS,
  FURNISHING_OPTIONS,
  INITIAL_FORM,
  OWNERSHIP_OPTIONS,
  TRANSACTION_OPTIONS,
} from "../constants";
import { getLocations, predictPrice } from "../services/api";
import ErrorBanner from "./ErrorBanner";
import LoadingSpinner from "./LoadingSpinner";
import ResultCard from "./ResultCard";

const NUMBER_FIELDS = new Set([
  "carpet_area_sqft",
  "floor_num",
  "Bathroom",
  "Balcony",
]);

function extractErrorMessage(error) {
  const detail = error?.response?.data?.detail;
  if (typeof detail === "string") {
    return detail;
  }
  if (Array.isArray(detail) && detail.length > 0) {
    return detail
      .map((item) => item.msg || JSON.stringify(item))
      .join(" ");
  }
  return error?.message || "Could not get a prediction. Please try again.";
}

export default function PredictionForm() {
  const [form, setForm] = useState(INITIAL_FORM);
  const [locations, setLocations] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;

    async function loadLocations() {
      try {
        const list = await getLocations();
        if (cancelled) {
          return;
        }
        setLocations(list);
        setForm((prev) => ({
          ...prev,
          location_grouped: prev.location_grouped || list[0] || "",
        }));
      } catch (err) {
        if (!cancelled) {
          setError(extractErrorMessage(err));
        }
      }
    }

    loadLocations();
    return () => {
      cancelled = true;
    };
  }, []);

  function handleChange(event) {
    const { name, value } = event.target;
    setForm((prev) => ({
      ...prev,
      [name]: NUMBER_FIELDS.has(name) ? Number(value) : value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await predictPrice(form);
      setResult(data);
    } catch (err) {
      setError(extractErrorMessage(err));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="card">
      <header className="card-header">
        <p className="eyebrow">India housing</p>
        <h1>House Price Predictor</h1>
        <p className="lead">
          Enter property details to estimate price in rupees, Lakh, and Crore.
        </p>
      </header>

      <form className="form-grid" onSubmit={handleSubmit}>
        <label>
          Carpet area (sqft)
          <input
            type="number"
            name="carpet_area_sqft"
            min="1"
            max="100000"
            step="1"
            value={form.carpet_area_sqft}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Floor number
          <input
            type="number"
            name="floor_num"
            min="0"
            max="200"
            value={form.floor_num}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Bathrooms
          <input
            type="number"
            name="Bathroom"
            min="0"
            max="20"
            value={form.Bathroom}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Balconies
          <input
            type="number"
            name="Balcony"
            min="0"
            max="20"
            value={form.Balcony}
            onChange={handleChange}
            required
          />
        </label>

        <label className="span-2">
          Location
          <select
            name="location_grouped"
            value={form.location_grouped}
            onChange={handleChange}
            required
          >
            {locations.length === 0 && (
              <option value="">Loading locations...</option>
            )}
            {locations.map((location) => (
              <option key={location} value={location}>
                {location}
              </option>
            ))}
          </select>
        </label>

        <label>
          Furnishing
          <select
            name="Furnishing"
            value={form.Furnishing}
            onChange={handleChange}
          >
            {FURNISHING_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label>
          Transaction
          <select
            name="Transaction"
            value={form.Transaction}
            onChange={handleChange}
          >
            {TRANSACTION_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label>
          Ownership
          <select
            name="Ownership"
            value={form.Ownership}
            onChange={handleChange}
          >
            {OWNERSHIP_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label>
          Facing
          <select name="facing" value={form.facing} onChange={handleChange}>
            {FACING_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <button className="submit-btn span-2" type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict Price"}
        </button>
      </form>

      {loading && <LoadingSpinner />}
      <ErrorBanner message={error} />
      <ResultCard result={result} />
    </div>
  );
}
