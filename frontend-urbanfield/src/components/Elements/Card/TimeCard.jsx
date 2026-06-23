import React from 'react';

const TimeCard = ({ startTime, endTime, price, isSelected, onSelect, isBooked }) => {
    let statusClass = isSelected ? "bg-sky-900 text-white" : "bg-white text-black";
    if (isBooked) {
        statusClass = "bg-gray-200 text-gray-400 cursor-not-allowed";
    }

    return (
        <div
            className={`border border-black rounded-xl font-Poppins font-semibold text-center p-4 ${isBooked ? '' : 'cursor-pointer'} ${statusClass}`}
            onClick={isBooked ? undefined : onSelect}
        >
            <span className="">60 Menit</span>
            <h3 className="text-xl">{startTime} - {endTime}</h3>
            <p className="text-lg">{isBooked ? 'Penuh' : price}</p>
        </div>
    )
}

export default TimeCard;
