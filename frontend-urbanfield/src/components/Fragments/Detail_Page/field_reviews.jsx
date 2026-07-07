import React, { useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";
import ReviewCard from "../../Elements/Card/ReviewCard";
import axios from "axios";
import { useModal } from "../../../context/ModalContext";


const FieldReviews = ({ fieldId }) => {
    const [reviews, setReviews] = useState([]);
    const [rating, setRating] = useState(10);
    const [reviewText, setReviewText] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const { showAlert } = useModal();

    useEffect(() => {
        fetchReviews();
    }, [fieldId]);

    const fetchReviews = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/fields/${fieldId}/reviews`);
            setReviews(response.data);
        } catch (error) {
            console.error("Error fetching reviews:", error);
        }
    };

    const handleSubmitReview = async (e) => {
        e.preventDefault();

        const token = localStorage.getItem('token');
        if (!token) {
            await showAlert('Silakan login terlebih dahulu untuk memberi review.', 'Butuh Login');
            window.location.href = '/login';
            return;
        }

        if (!reviewText.trim()) {
            await showAlert('Tulis review Anda terlebih dahulu.', 'Ulasan Kosong');
            return;
        }

        try {
            setSubmitting(true);
            await axios.post('http://127.0.0.1:5000/field_reviews', {
                field_id: fieldId,
                rating: Number(rating),
                review: reviewText,
            });

            setReviewText('');
            setRating(10);
            fetchReviews();
        } catch (error) {
            console.error('Error submitting review:', error);
            await showAlert('Gagal mengirim review. Silakan coba lagi.', 'Error');
        } finally {
            setSubmitting(false);
        }
    };

    return (
        <div className="mt-20 mx-56 mb-60">
            <div className="flex items-center ml-2">
                <img src="/img/reviewIcon.png" alt="review" className="w-14" />
                <h2 className="ml-5 text-4xl font-Poppins font-semibold">Reviews</h2>
            </div>

            <form onSubmit={handleSubmitReview} className="mt-8 mx-2 border border-gray-300 rounded-lg p-5">
                <h3 className="font-Poppins font-semibold text-lg mb-3">Beri Review</h3>
                <label className="block text-sm font-medium text-gray-700 mb-1">Rating (1-10):</label>
                <input
                    type="number"
                    min="1"
                    max="10"
                    value={rating}
                    onChange={(e) => setRating(e.target.value)}
                    className="block w-24 p-2 border border-gray-300 rounded mb-3"
                />
                <label className="block text-sm font-medium text-gray-700 mb-1">Review:</label>
                <textarea
                    value={reviewText}
                    onChange={(e) => setReviewText(e.target.value)}
                    rows={3}
                    className="block w-full p-2 border border-gray-300 rounded mb-3"
                    placeholder="Bagaimana pengalaman Anda di lapangan ini?"
                />
                <button
                    type="submit"
                    disabled={submitting}
                    className="bg-sky-900 hover:bg-sky-800 text-white font-semibold py-2 px-6 rounded-lg disabled:opacity-50"
                >
                    {submitting ? 'Mengirim...' : 'Kirim Review'}
                </button>
            </form>

            <div className="flex gap-48 mt-8 flex-wrap">
                {reviews.length === 0 ? (
                    <p className="text-gray-500 mx-2">Belum ada review untuk lapangan ini.</p>
                ) : (
                    reviews.map((review) => (
                        <ReviewCard
                            key={review.id}
                            name="Anonim"
                            rating={review.rating}
                            review={review.review}
                        />
                    ))
                )}
            </div>
        </div>
    );
};

export default FieldReviews;