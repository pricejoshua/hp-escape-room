class SerpentineCipher:
    def __init__(self):
        # mapping dictionaries for encoding and decoding
        self.encode_map = {
            'a': 'ᚨ',
            'b': 'ξ',
            'c': 'λ',
            'd': 'ᛞ',
            'e': 'ᛋ',
            'f': 'ᚠ',
            'g': 'ว',
            'h': 'ᚺ',
            'i': 'ఠ',
            'j': 'ᛃ',
            'k': 'ᚴ',
            'l': 'ᛚ',
            'm': 'Թ',
            'n': 'ᚾ',
            'o': 'ᛟ',
            'p': 'ᛈ',
            'q': 'ᚦ',
            'r': 'ຣ',
            's': 'ᛢ',
            't': 'ᛏ',
            'u': 'ᚢ',
            'v': 'ᚡ',
            'w': 'ᚹ',
            'x': 'ᛪ',
            'y': 'ᛦ',
            'z': 'ᛉ',
            ' ': ' '
        }
        self.decode_map = {v: k for k, v in self.encode_map.items()}
    
    def encode(self, text: str) -> str:
        """Convert regular text to serpentine runes."""
        return ''.join(self.encode_map.get(c.lower(), c) for c in text)
    
    def decode(self, encoded: str) -> str:
        """Convert serpentine runes back to regular text."""
        return ''.join(self.decode_map.get(c, c) for c in encoded)

# Example usage
if __name__ == "__main__":
    cipher = SerpentineCipher()
    
    # Test encoding
    text = "RESEARCH CLEARANCE GRANTED FOR ADVANCED STUDY OF: SERPENTINE LANGUAGE AND VOCAL MANIFESTATIONS IN MAGICAL CREATURES"
    text = "Name of book"
    encoded = cipher.encode(text)
    print(f"Encoded: {encoded}")
    
    # Test decoding
    decoded = cipher.decode(encoded)
    print(f"Decoded: {decoded}")