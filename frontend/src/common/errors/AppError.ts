export class AppError extends Error {
  constructor(
    public readonly name: string,
    public readonly originalError: unknown,
    message: string,
  ) {
    super(message);

    if (originalError instanceof Error && originalError.stack) this.stack = originalError.stack;
  }
}

export function isAppError(err: unknown): err is AppError {
  return err instanceof AppError;
}
