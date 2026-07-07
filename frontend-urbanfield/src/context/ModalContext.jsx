import React, { createContext, useContext, useState } from 'react';

const ModalContext = createContext(null);

export const ModalProvider = ({ children }) => {
    const [modal, setModal] = useState({
        isOpen: false,
        type: 'alert', // 'alert' or 'confirm'
        message: '',
        title: '',
        onConfirm: null,
        onCancel: null,
    });

    const showAlert = (message, title = 'Pemberitahuan') => {
        return new Promise((resolve) => {
            setModal({
                isOpen: true,
                type: 'alert',
                message,
                title,
                onConfirm: () => {
                    setModal(prev => ({ ...prev, isOpen: false }));
                    resolve(true);
                },
                onCancel: null
            });
        });
    };

    const showConfirm = (message, title = 'Konfirmasi') => {
        return new Promise((resolve) => {
            setModal({
                isOpen: true,
                type: 'confirm',
                message,
                title,
                onConfirm: () => {
                    setModal(prev => ({ ...prev, isOpen: false }));
                    resolve(true);
                },
                onCancel: () => {
                    setModal(prev => ({ ...prev, isOpen: false }));
                    resolve(false);
                }
            });
        });
    };

    return (
        <ModalContext.Provider value={{ showAlert, showConfirm }}>
            {children}
            {modal.isOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 transition-opacity duration-300">
                    <div className="bg-white rounded-2xl shadow-2xl p-6 w-96 transform scale-100 transition-transform duration-300 border border-slate-100 font-Poppins">
                        {/* Title & Icon */}
                        <div className="flex items-center space-x-3 mb-4">
                            {modal.type === 'confirm' ? (
                                <div className="w-10 h-10 flex items-center justify-center bg-amber-100 text-amber-600 rounded-full">
                                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                    </svg>
                                </div>
                            ) : (
                                <div className="w-10 h-10 flex items-center justify-center bg-blue-100 text-blue-600 rounded-full">
                                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                            )}
                            <h3 className="text-lg font-bold text-gray-900">{modal.title}</h3>
                        </div>

                        {/* Message */}
                        <p className="text-gray-600 text-sm mb-6 leading-relaxed">
                            {modal.message}
                        </p>

                        {/* Action Buttons */}
                        <div className="flex justify-end space-x-3">
                            {modal.type === 'confirm' && (
                                <button
                                    onClick={modal.onCancel}
                                    className="px-4 py-2 border border-gray-300 rounded-xl text-gray-700 text-sm font-medium hover:bg-gray-50 transition-colors"
                                >
                                    Batal
                                </button>
                            )}
                            <button
                                onClick={modal.onConfirm}
                                className="px-5 py-2 bg-sky-900 text-white rounded-xl text-sm font-medium hover:bg-sky-800 transition-colors shadow-md"
                            >
                                Ya, Lanjutkan
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </ModalContext.Provider>
    );
};

export const useModal = () => {
    const context = useContext(ModalContext);
    if (!context) {
        throw new Error('useModal must be used within a ModalProvider');
    }
    return context;
};
