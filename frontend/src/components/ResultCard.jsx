function formatRupees(value) {
  return Number(value).toLocaleString("en-IN", {
    maximumFractionDigits: 0,
  });
}

function formatUnits(value) {
  return Number(value).toLocaleString("en-IN", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
}

export default function ResultCard({ result }) {
  if (!result) {
    return null;
  }

  return (
    <section className="result-card">
      <h2>Predicted Price</h2>
      <p className="price-main">₹ {formatRupees(result.predicted_price)}</p>
      <p className="price-sub">
        {formatUnits(result.predicted_price_lac)} Lac ·{" "}
        {formatUnits(result.predicted_price_cr)} Cr
      </p>
    </section>
  );
}
