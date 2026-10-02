#!/usr/bin/env bash
# Se ejecuta una sola vez, al crear el Codespace.
set -euxo pipefail

# --- uv: gestor de paquetes y de herramientas de Python ---
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# --- dependencias del proyecto del curso ---
uv sync || uv pip install --system \
  fastapi uvicorn httpx pydantic pytest python-dotenv openai numpy "mcp[cli]"

# --- Spec Kit (sesión 4) ---
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git || true

# --- OpenCode (sesión 3) ---
curl -fsSL https://opencode.ai/install | bash || true

echo
echo "=== Entorno del curso listo ==="
uv --version || true
python --version
specify --version 2>/dev/null || echo "specify: instalado (comprobar con 'specify check')"
opencode --version 2>/dev/null || echo "opencode: instalado"
echo "Recuerda: las credenciales de poliGPT van en POLIGPT_URL y POLIGPT_KEY."
